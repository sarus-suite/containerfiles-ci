# HPC Comm Stack CUDA Container

A minimal container image based on `nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04` with:

- GDRCopy v2.5.1
- libfabric v1.22.0 (CUDA‐dlopen, GDRCopy‐dlopen, EFA)
- UCX v1.19.0 (CUDA, GDRCopy, multithread, developer headers)

## Building
~~~
podman build \
  --build-arg ubuntu_version=24.04 \
  --build-arg cuda_version=12.8.1 \
  --build-arg gdrcopy_version=2.5.1 \
  --build-arg libfabric_version=1.22.0 \
  --build-arg UCX_VERSION=1.19.0 \
  -t hpc-comm-cuda .
~~~
