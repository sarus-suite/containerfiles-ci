# PyFR MPI/CUDA Container

A lightweight container image based on `quay.io/ethcscs/ompi:5.0.7-ofi1.15-cuda12.8` with:

- OpenMPI 5.0.7 + libfabric 1.15  
- CUDA 12.8  
- Parallel HDF5 1.14.6  
- libxsmm  
- Python 3 with h5py (MPI‐enabled) and PyFR 2.1  

## Build

You can override the HDF5 version:

~~~
podman build \
  --build-arg HDF5_VERSION=1.12.1 \
  -t pyfr-mpi-cuda .
~~~
