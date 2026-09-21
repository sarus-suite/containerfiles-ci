# MPICH based on Comm Stack CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/comm-fwk:ofi2.6.0-ucx1.22.0-cuda13.4.1` with:

- MPICH 5.0.1 built with CH4/OFI and XPMEM support
- CUDA support for Compute Capabilities 8.0, 8.6, 8.9, 9.0, 9.0a, 10.0, 10.3 (Ampere to Blackwell; CUDA 13 removed support for capabilities <7.5)
- Fast O3/ndebug optimizations  
- C++ bindings disabled

## Building
~~~
podman build \
  --build-arg MPI_VER=5.0.1 \
  -t mpich .
~~~
