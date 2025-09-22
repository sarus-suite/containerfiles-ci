# NCCL-Tests MPI/CUDA Container

A minimal container image based on `quay.io/ethcscs/ompi:5.0.8-ofi1.22-cuda12.8` with:

- MPI-enabled NCCL-Tests v2.17.1

## Building
~~~
podman build \
  --build-arg nccl_tests_version=2.17.1 \
  -t nccl-tests-mpi-cuda .
~~~
