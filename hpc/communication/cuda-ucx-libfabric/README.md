# HPC Comm Stack CUDA Container

A minimal container image based on `nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04` with:

- GDRCopy v2.4.4  
- libfabric v1.15.0 (CUDA‐dlopen, GDRCopy‐dlopen, EFA)  
- UCX v1.18.0 (CUDA, GDRCopy, multithread, developer headers)  

## Building
~~~
podman build \
  --build-arg ubuntu_version=24.04 \
  --build-arg cuda_version=12.1.8 \
  --build-arg gdrcopy_version=2.4.4 \
  --build-arg libfabric_version=1.15.0 \
  --build-arg UCX_VERSION=1.18.0 \
  -t hpc-comm-cuda .
~~~
