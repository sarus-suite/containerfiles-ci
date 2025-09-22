# OSU Micro-Benchmarks OpenMPI/CUDA Container

A minimal container image based on `quay.io/ethcscs/ompi:5.0.8-ofi1.22-cuda12.8` with:

- OpenMPI 5.0.8 + libfabric 1.22
- CUDA 12.8  
- OSU Micro-Benchmarks v7.5.1 (MPI + CUDA enabled)

## Building 
~~~
podman build \
  --build-arg omb_version=7.5.1 \
  -t osu-micro-openmpi-cuda .
~~~
