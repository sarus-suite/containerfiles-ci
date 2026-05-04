# OSU Micro-Benchmarks MPICH/CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/mpich:4.3.2-ofi1.22-cuda12.8.1` with:

- MPICH 4.3.2 + libfabric 1.22
- CUDA 12.8  
- OSU Micro-Benchmarks v7.5.2 (MPI + CUDA enabled)  

## Building
~~~
podman build \
  --build-arg omb_version=7.5.2 \
  -t osu-micro-mpich-cuda .
~~~
