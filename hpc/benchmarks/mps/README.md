# CUDA Samples + MPS Overlap Test Container

A minimal CUDA development container that:
* Builds and ships matrixMulCUBLAS from NVIDIA’s CUDA Samples with larger problem sizes and more iterations for longer runtime.
* Compiles a tiny CUDA spin-kernel program (mps\_overlap\_test) you can use to sanity-check GPU visibility and experiment with CUDA MPS / kernel overlap.

Base image: nvcr.io/nvidia/cuda:12.5.0-devel-ubuntu22.04

