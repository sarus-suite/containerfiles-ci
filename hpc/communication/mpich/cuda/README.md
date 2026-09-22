# MPICH based on Comm Stack CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/comm-fwk:ofi1.22.0-ucx1.20.0-cuda12.8.1` with:

- MPICH 4.3.2 built with CH4/OFI and CUDA support  
- Fast O3/ndebug optimizations  
- Fortran & C++ bindings disabled  

## Building
~~~
podman build \
  --build-arg MPI_VER=4.3.2 \
  -t mpich .
~~~
