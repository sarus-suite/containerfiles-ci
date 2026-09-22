# HPC Communication Frameworks Container

A minimal container image based on `docker.io/library/ubuntu:24.04` with:

- XPMEM v2.6.5-36 (commit 0d0bad4e1d)
- libfabric v2.6.0
- UCX v1.22.0 (multithread, developer headers)

## Building
~~~
podman build \
  --build-arg ubuntu_version=24.04 \
  --build-arg libfabric_version=2.6.0 \
  --build-arg ucx_version=1.22.0 \
  -t comm-fwk .
~~~
