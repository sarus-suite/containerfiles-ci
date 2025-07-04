# OSU Micro-Benchmarks OpenMPI/CUDA Container

A minimal container image based on `quay.io/ethcscs/ompi:5.0.7-ofi1.15-cuda12.8` with:

- OpenMPI 5.0.7 + libfabric 1.15  
- CUDA 12.8  
- OSU Micro-Benchmarks v7.5 (MPI + CUDA enabled)  

## Building 
~~~
podman build \
  --build-arg omb_version=7.5 \
  -t osu-micro-openmpi-cuda .
~~~
