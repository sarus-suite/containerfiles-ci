import os, json, time, argparse, math
from datetime import datetime, timezone

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def get_dtype():
    if torch.cuda.is_available():
        if torch.cuda.is_bf16_supported():
            return torch.bfloat16
        if torch.cuda.is_available():
            return torch.float16
    return torch.float32

def get_context_window(model, tokenizer):
    ctx = getattr(model.config, "max_position_embeddings", None)
    if ctx is None or (isinstance(ctx, int) and ctx > 10_000_000):
        ctx = getattr(tokenizer, "model_max_length", 4096)
    if isinstance(ctx, int) and ctx > 10_000_000:
        ctx = 4096
    return int(ctx)

def read_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def count_tokens(tokenizer, text):
    return len(tokenizer(text, add_special_tokens=False).input_ids)

def per_device_max_mem_mb():
    if not torch.cuda.is_available():
        return {}
    out = {}
    for i in range(torch.cuda.device_count()):
        torch.cuda.reset_peak_memory_stats(i)
    return out

def current_device_peaks_mb():
    if not torch.cuda.is_available():
        return {}
    out = {}
    for i in range(torch.cuda.device_count()):
        peak = torch.cuda.max_memory_allocated(i) / (1024**2)
        out[f"cuda:{i}"] = round(peak, 2)
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="swiss-ai/Apertus-8B-Instruct-2509")
    parser.add_argument("--prompt-file", default="/data/prompt.txt")
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--truncate", action="store_true",
                        help="If prompt exceeds context window, keep the last N tokens.")
    parser.add_argument("--out-text", default="/output/output.txt")
    parser.add_argument("--out-json", default="/output/metrics.json")
    parser.add_argument("--append-jsonl", default="/output/bench.jsonl")
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True

    dtype = get_dtype()
    model_id = args.model

    tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
    if tokenizer.pad_token_id is None and tokenizer.eos_token_id is not None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Loading model: {model_id} (dtype={dtype})")
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=dtype,
        device_map="auto",
    )
    model.eval()

    ctx_window = get_context_window(model, tokenizer)
    prompt = read_prompt(args.prompt_file)

    enc = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
    input_ids = enc.input_ids
    input_len = input_ids.shape[1]

    if input_len > ctx_window:
        if args.truncate:
            input_ids = input_ids[:, -ctx_window:]
            print(f"[warn] Prompt had {input_len} tokens; truncated to last {ctx_window}.")
            input_len = ctx_window
        else:
            raise ValueError(
                f"Prompt has {input_len} tokens, exceeds context window {ctx_window}. "
                f"Re-run with --truncate to auto-trim."
            )

    _ = per_device_max_mem_mb()
    if torch.cuda.is_available():
        torch.cuda.synchronize()

    gen_kwargs = dict(
        max_new_tokens=args.max_new_tokens,
        do_sample=True if args.temperature > 0 else False,
        temperature=args.temperature,
        top_p=args.top_p,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.pad_token_id,
        use_cache=True,
    )

    t0 = time.perf_counter()
    input_ids = input_ids.to(model.device)
    with torch.inference_mode():
        outputs = model.generate(input_ids=input_ids, **gen_kwargs)
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    t1 = time.perf_counter()

    total_time = t1 - t0
    new_tokens = outputs.shape[1] - input_len
    toks_per_sec = (new_tokens / total_time) if total_time > 0 else float("nan")

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    with open(args.out_text, "w", encoding="utf-8") as f:
        f.write(text)
    gpu_mem = current_device_peaks_mb()
    metrics = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model_id,
        "dtype": str(dtype).replace("torch.", ""),
        "device_map": "auto",
        "prompt_file": args.prompt_file,
        "input_tokens": int(input_len),
        "output_tokens": int(new_tokens),
        "total_time_s": round(total_time, 4),
        "tokens_per_sec": round(toks_per_sec, 2),
        "gen_params": {
            "max_new_tokens": args.max_new_tokens,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "seed": args.seed,
            "truncate": bool(args.truncate),
            "context_window": ctx_window,
        },
        "gpu_peak_mem_mb": gpu_mem,
        "out_text": args.out_text,
    }

    with open(args.out_json, "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)
    with open(args.append_jsonl, "a", encoding="utf-8") as f:
        f.write(json.dumps(metrics, ensure_ascii=False) + "\n")

    # Short console summary
    print(
        f"[done] in {metrics['total_time_s']}s | "
        f"in:{metrics['input_tokens']} tok → out:{metrics['output_tokens']} tok | "
        f"{metrics['tokens_per_sec']} tok/s | peaks: {gpu_mem}"
    )

if __name__ == "__main__":
    main()

