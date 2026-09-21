# NCCL-Tests MPI/CUDA Container

A minimal container image based on `quay.io/ethcscs/ompi:5.0.11-ofi2.6.0-cuda13.4.1` with:

- MPI-enabled NCCL-Tests v2.20.0 

## Building
~~~
podman build \
  --build-arg nccl_tests_version=2.20.0 \
  -t nccl-tests-mpi-cuda .
~~~
