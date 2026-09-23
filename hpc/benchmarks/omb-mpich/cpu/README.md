# OSU Micro-Benchmarks MPICH CPU Container

A minimal container image based on `ghcr.io/sarus-suite/containerfiles-ci/mpich:5.0.1-ofi2.6.0` with:

- MPICH 4.3.2 + libfabric 2.6.0
- OSU Micro-Benchmarks v7.5.2 

## Building
~~~
podman build \
  --build-arg omb_version=7.5.2 \
  -t osu-micro-mpich-cuda .
~~~
