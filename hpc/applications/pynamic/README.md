# Pynamic MPI Container

A minimal container image based on `debian:trixie` with:

- libfabric 1.22.0
- OpenMPI 5.0.9
- Python 3 + mpi4py
- Pynamic-pyMPI (fork: `https://github.com/Madeeks/pynamic` - branch: `fixes` - commit: `5a0aac1`)

## Building
~~~
podman build \
  --build-arg LIBFABRIC_VERSION=1.22.0 \
  --build-arg MPI_VERSION=5.0.9 \
  --build-arg MPI_SHORT_VERSION=5.0 \
  -t pynamic-mpi .
~~~
