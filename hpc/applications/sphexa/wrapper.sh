#!/bin/bash
export LOCAL_RANK=$SLURM_LOCALID
export GLOBAL_RANK=$SLURM_PROCID
export GPUS=(0 1 2 3)
export NUMA_NODE=$((LOCAL_RANK % 4))
export CUDA_VISIBLE_DEVICES=${GPUS[$NUMA_NODE]}

numactl --cpunodebind=$NUMA_NODE --membind=$NUMA_NODE "$@"
