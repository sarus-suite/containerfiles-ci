# Slurm build image 

A container to build slurm plugins like skybox

## Building
~~~
OS_NAME="ubuntu"
OS_VERSION="24.04"
SLURM_VERSION="25.05.4-1"

podman build \
  --build-arg os_version=${OS_VERSION} \
  --build-arg slurm_version=${SLURM_VERSION} \
  -f ubuntu/Containerfile \
  -t build-slurm-${OS_NAME} \
  .
~~~
