# OSU Micro-Benchmarks MPICH/CUDA Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/mpich:5.0.1-ofi2.6.0-cuda13.4.1` with:

- MPICH 5.0.1 + libfabric 2.6.0
- CUDA 13.4  
- OSU Micro-Benchmarks v7.5.2 (MPI + CUDA enabled)  

## Building
~~~
podman build \
  --build-arg omb_version=7.5.2 \
  -t osu-micro-mpich-cuda .
~~~
