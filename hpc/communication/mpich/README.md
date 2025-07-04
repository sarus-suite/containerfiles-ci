# MPICH based on Comm Stack CUDA Container

A minimal container image based on `quay.io/ethcscs/comm-fwk:ofi1.15-ucx1.18-cuda12.8` with:

- MPICH 4.3.0 built with CH4/OFI and CUDA support  
- Fast O3/ndebug optimizations  
- Fortran & C++ bindings disabled  

## Building
~~~
podman build \
  --build-arg MPI_VER=4.3.0 \
  -t mpich-comm-fwk .
~~~
