# NCCL-Tests MPI/CUDA Container

A minimal container image based on `quay.io/ethcscs/ompi:5.0.7-ofi1.15-cuda12.8` with:

- MPI-enabled NCCL-Tests v2.14.1  

## Building
~~~
podman build \
  --build-arg nccl_tests_version=2.14.1 \
  -t nccl-tests-mpi-cuda .
~~~
