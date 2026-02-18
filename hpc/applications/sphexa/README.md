# SPH-EXA MPI/CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/mpich:4.3.2-ofi1.22-cuda12.8.1` with:

- Parallel HDF5 (MPI-enabled)  
- SPH-EXA v0.95 with GPU-aware MPI  

## Building
~~~
podman build \
  --build-arg HDF5_VERSION=1.14.6 \
  --build-arg sph_exa_version=0.95 \
  -t sph-exa-mpi-cuda .
~~~
