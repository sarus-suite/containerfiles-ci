# OSU Micro-Benchmarks MPI/CUDA Container

A minimal container image based on `quay.io/ethcscs/mpich:4.3.0-ofi1.15-cuda12.8` with:

- MPICH 4.3.0 + libfabric 1.15  
- CUDA 12.8  
- OSU Micro-Benchmarks v7.5 (MPI + CUDA enabled)  

## Building
~~~
podman build \
  --build-arg omb_version=7.5 \
  -t osu-micro-mpich-cuda .
~~~
