# MPICH based on Comm Stack CPU Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/comm-fwk:ofi2.6.0-ucx1.22.0` with:

- MPICH 5.0.1 built with CH4/OFI and XPMEM support  
- Fast O3/ndebug optimizations  
- C++ bindings disabled  

## Building
~~~
podman build \
  --build-arg MPI_VER=5.0.1 \
  -t mpich .
~~~
