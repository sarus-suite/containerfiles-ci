# OpenMPI based on Comm Stack CUDA Container

A minimal container image based on `quay.io/ethcscs/comm-fwk:ofi1.15-ucx1.18-cuda12.8` with:

- OpenMPI 5.0.7 built against libfabric (OFI) and UCX  
- OSHMEM support  
- CUDA 12.8
- UCX 1.18
- Libfabric 1.15

## Building
~~~
podman build \
  --build-arg OMPI_VER=5.0.7 \
  -t openmpi-comm-fwk-cuda .
~~~
