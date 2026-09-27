# HPC Communication Frameworks CUDA Container

A minimal container image based on `nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04` with:

- GDRCopy v2.5.1
- libfabric v1.22.0 (CUDA‐dlopen, GDRCopy‐dlopen, EFA)
- UCX v1.18.0 (CUDA, GDRCopy, multithread, developer headers)

## Building
~~~
podman build \
  --build-arg ubuntu_version=24.04 \
  --build-arg cuda_version=12.8.1 \
  --build-arg gdrcopy_version=2.5.1 \
  --build-arg libfabric_version=1.22.0 \
  --build-arg ucx_version=1.20.0 \
  --build-arg ucc_version=1.6.0
  -t comm-fwk-cuda .
~~~
