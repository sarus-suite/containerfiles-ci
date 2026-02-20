# SPH-EXA MPI/CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/mpich:4.3.2-ofi1.22-cuda12.8.1` with:

- Parallel HDF5 (MPI-enabled)  
- SPH-EXA v0.95 with GPU-aware MPI

The image also sets `/sphexa` as its initial working directory, where useful assets for running SPH-EXA are provided:
- The [50c.h5](https://zenodo.org/records/8369645)  template glass block for initial conditions generation (a template particle distribution is required for the Evrard test case)
- A bash wrapper script to perform appropriate CPU/memory NUMA bindings for ranks in Slurm-managed nodes with 4 NVIDIA GPUs. Usage: `./wrapper.sh sphexa-cuda [...]`

## Building
~~~
podman build \
  --build-arg HDF5_VERSION=1.14.6 \
  --build-arg sph_exa_version=0.95 \
  -t sph-exa-mpi-cuda .
~~~
