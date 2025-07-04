# Pynamic MPI Container

A minimal container image based on `debian:bookworm` with:

- libfabric 1.15.1  
- OpenMPI 5.0.7  
- Python 3 + mpi4py  
- Pynamic-pyMPI (branch: `fixes`)  

## Building
~~~
podman build \
  --build-arg LIBFABRIC_VERSION=1.15.1 \
  --build-arg MPI_VERSION=5.0.7 \
  --build-arg MPI_SHORT_VERSION=5.0 \
  --build-arg IMAGE_ARCH=x86_64 \
  -t pynamic-mpi .
~~~
