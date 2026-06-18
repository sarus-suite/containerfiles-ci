# Opensuse Slurm build image 

A container to build slurm plugins like skybox on opensuse

## Building
~~~
podman build \
  --build-arg os_version=15.6 \
  --build-arg slurm_version=25.05.4-1 \
  -t build-slurm-opensuse .
~~~
