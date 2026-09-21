# HPC Communication Frameworks CUDA Container

A minimal container image based on `nvidia/cuda:13.4.1-cudnn-devel-ubuntu24.04` with:

- GDRCopy v2.6
- XPMEM v2.6.5-36 (commit 0d0bad4e1d)
- libfabric v2.6.0 (CUDA‐dlopen, GDRCopy‐dlopen, EFA)
- UCX v1.22.0 (CUDA, GDRCopy, multithread, developer headers)

## Building
~~~
podman build \
  --build-arg ubuntu_version=24.04 \
  --build-arg cuda_version=13.4.1 \
  --build-arg xpmem_ref=0d0bad4e1d07b38d53ecc8f20786bb1328c446da \
  --build-arg gdrcopy_version=2.6 \
  --build-arg libfabric_version=2.6.0 \
  --build-arg ucx_version=1.22.0
  -t comm-fwk-cuda .
~~~
