# OSU Micro-Benchmarks MPI/CUDA Container

A minimal container image based on `quay.io/ethcscs/mpich:4.3.1-ofi1.22-cuda12.8` with:

- MPICH 4.3.1 + libfabric 1.22
- CUDA 12.8  
- OSU Micro-Benchmarks v7.5.1 (MPI + CUDA enabled)

## Building
~~~
podman build \
  --build-arg omb_version=7.5.1 \
  -t osu-micro-mpich-cuda .
~~~
