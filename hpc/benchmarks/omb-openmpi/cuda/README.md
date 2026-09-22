# OSU Micro-Benchmarks OpenMPI/CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/ompi:5.0.9-ofi1.22.0-cuda12.8.1` with:

- OpenMPI 5.0.9 + libfabric 1.22
- CUDA 12.8
- OSU Micro-Benchmarks v7.5.2 (MPI + CUDA enabled)

## Building 
~~~
podman build \
  --build-arg omb_version=7.5.2 \
  -t osu-micro-openmpi-cuda .
~~~
