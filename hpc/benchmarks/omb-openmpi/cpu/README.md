# OSU Micro-Benchmarks OpenMPI CPU Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/ompi:5.0.11-ofi2.6.0` with:

- OpenMPI 5.0.11 + libfabric 2.6.0
- OSU Micro-Benchmarks v7.5.2 (MPI + CUDA enabled)

## Building 
~~~
podman build \
  --build-arg omb_version=7.5.2 \
  -t osu-micro-openmpi-cuda .
~~~
