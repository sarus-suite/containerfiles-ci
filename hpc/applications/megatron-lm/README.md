# Megatron-LM PyTorch Container

A container image providing [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) and Megatron Core based on [NVIDIA NGC PyTorch images](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch).
Current features:

- Megatron Core/ Megatron-LM 0.15.2
- NGC PyTorch 25.11 (CUDA 13.0.2)

## Build

~~~
podman build \
  --build-arg ngc_pytorch_version=25.12 \
  --build-arg megatron_core_version=0.15.2 \
  -t megatron-lm .
~~~