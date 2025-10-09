# Transformers Benchmark Container

A minimal container image based on `nvcr.io/nvidia/pytorch:24.01-py3` with:

- PyTorch 2.2 (CUDA 12.x)
- Hugging Face Transformers ≥ 4.44.0
- Tokenizers ≥ 0.20.0, Accelerate ≥ 1.0.0, HuggingFace Hub ≥ 0.25.0  
- Custom library: [`xielu`](https://github.com/rubber-duck-debug/xielu)
- Includes `benchmark_infer.py` for model inference benchmarking

## Building
```bash
podman build -t transformers-bench .
````

## Running

Example benchmark run:

```bash
podman run --gpus all --rm \
  -v $PWD/data:/data:ro \
  -v $PWD/output:/output \
  transformers-bench \
  python benchmark_infer.py \
    --model swiss-ai/Apertus-8B-Instruct-2509 \
    --prompt-file /data/prompt.txt \
    --max-new-tokens 1024
```

Outputs:

* `/output/output.txt` – generated text
* `/output/metrics.json` – run metrics (JSON)
* `/output/bench.jsonl` – append-only benchmark log


