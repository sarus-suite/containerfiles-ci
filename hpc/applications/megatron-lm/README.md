# Megatron-LM PyTorch Container

A container image providing [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) and Megatron Core based on [NVIDIA NGC PyTorch images](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch).
Current features:

- Megatron Core/ Megatron-LM 0.19.2
- NGC PyTorch 26.08 (CUDA 13.4.1)

## Build

~~~
podman build \
  --build-arg ngc_pytorch_version=26.108 \
  --build-arg megatron_core_version=0.19.2 \
  -t megatron-lm .
~~~