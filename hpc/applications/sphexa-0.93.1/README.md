# SPH-EXA MPI/CUDA Container

A minimal container image based on `quay.io/ethcscs/ompi:5.0.7-ofi1.15-cuda12.8` with:

- Parallel HDF5 (MPI-enabled)  
- SPH-EXA v0.93.1 with GPU-aware MPI  

## Building
~~~
podman build \
  --build-arg HDF5_VERSION=1.14.6 \
  --build-arg sph_exa_version=0.93.1 \
  -t sph-exa-mpi-cuda .
~~~
