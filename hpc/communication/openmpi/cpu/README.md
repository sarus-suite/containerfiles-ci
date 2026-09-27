# OpenMPI based on Comm Stack CPU Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/comm-fwk:ofi2.6.0-ucx1.22.0` with:

- OpenMPI 5.0.11 built against libfabric (OFI) and UCX  
- OSHMEM support
- Libfabric 2.6.0
- UCX 1.22

## Building
~~~
podman build \
  --build-arg OMPI_VER=5.0.11 \
  -t openmpi .
~~~
