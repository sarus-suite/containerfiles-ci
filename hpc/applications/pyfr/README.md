# PyFR MPI/CUDA Container

A lightweight container image based on `ghcr.io/sarus-suite/containerfiles-ci/ompi:5.0.9-ofi1.22-cuda12.8.1` with:

- OpenMPI 5.0.9 + libfabric 1.22
- CUDA 12.8
- Parallel HDF5 1.14.6
- libxsmm
- Python 3 with h5py (MPI‐enabled) and PyFR 2.1

## Build

**Note: the build step for HDF5 uses autotools, and therefore does not support HDF5 >=2.0.0**

~~~
podman build \
  --build-arg HDF5_VERSION=1.14.6 \
  --build-arg pyfr_version=2.1 \
  -t pyfr-mpi-cuda .
~~~
