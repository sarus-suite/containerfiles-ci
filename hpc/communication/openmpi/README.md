# OpenMPI based on Comm Stack CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/comm-fwk:ofi1.22.0-ucx1.20.0-cuda12.8.1` with:

- OpenMPI 5.0.9 built against libfabric (OFI) and UCX  
- OSHMEM support  
- CUDA 12.8
- UCX 1.20
- Libfabric 1.22

## Building
~~~
podman build \
  --build-arg OMPI_VER=5.0.9 \
  -t openmpi .
~~~
