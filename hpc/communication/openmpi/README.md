# OpenMPI based on Comm Stack CUDA Container

A minimal container image based on `quay.io/ethcscs/comm-fwk:ofi1.22-ucx1.19-cuda12.8` with:

- OpenMPI 5.0.8 built against libfabric (OFI) and UCX
- OSHMEM support
- CUDA 12.8
- UCX 1.19
- Libfabric 1.22

## Building
~~~
podman build \
  --build-arg OMPI_VER=5.0.8 \
  -t openmpi-comm-fwk-cuda .
~~~
