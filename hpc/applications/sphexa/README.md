# SPH-EXA MPI/CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/ompi:5.0.9-ofi1.22-cuda12.8.1` with:

- Parallel HDF5 2.1.1 (MPI-enabled)  
- SPH-EXA v0.96.2 with GPU-aware MPI

The image also sets `/sphexa` as its initial working directory, where useful assets for running SPH-EXA are provided:
- The [50c.h5](https://zenodo.org/records/8369645) template glass block for initial conditions generation (a template particle distribution is required for the Evrard test case)
- A bash wrapper script to perform appropriate CPU/memory NUMA bindings for ranks in Slurm-managed nodes with 4 NVIDIA GPUs. Usage: `./wrapper.sh sphexa-cuda [...]`

## Building
```
podman build \
  --build-arg HDF5_VERSION=2.1.1 \
  --build-arg sph_exa_version=0.96.2 \
  -t sph-exa-mpi-cuda .
```

## Benchmark quickstart

The image already packages the components needed for running SPH-EXA built-in test cases.
For example, in a system with 4 GPUs running Slurm:
```
srun --mpi=pmix --edf=sphexa --ntasks-per-node=4 /sphexa/wrapper.sh sphexa-cuda --init evrard --glass /sphexa/50c.h5 -n 200 -s 5
```

When using the glass file included in the image, the Open MPI IO implementation (OMPIO) might have problems, depending on the container runtime and the system used. In that case, OMPIO can be disabled by setting the `OMPI_MCA_io=^ompio` environment variable.
