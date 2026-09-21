# OSU Micro-Benchmarks OpenMPI/CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/ompi:5.0.11-ofi2.6.0-cuda13.4.1` with:

- OpenMPI 5.0.11 + libfabric 2.6.0
- CUDA 13.4.1
- OSU Micro-Benchmarks v7.5.2 (MPI + CUDA enabled)

## Building 
~~~
podman build \
  --build-arg omb_version=7.5.2 \
  -t osu-micro-openmpi-cuda .
~~~
