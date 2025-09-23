#include <cuda_runtime.h>
#include <stdio.h>
#include <chrono>

#define CHECK(call) do { \
    cudaError_t err__ = (call); \
    if (err__ != cudaSuccess) { \
        fprintf(stderr, "CUDA error %s:%d: %s (%d)\n", __FILE__, __LINE__, cudaGetErrorString(err__), err__); \
        exit(1); \
    } \
} while (0)

__global__ void spin_kernel(unsigned long long iters, unsigned long long *out) {
    unsigned long long counter = 0;
    for (unsigned long long i = 0; i < iters; i++) {
        asm volatile("" ::: "memory"); // compiler barrier: don't collapse the loop
        counter++;
    }
    out[0] = counter; // single observable store
}

int main(int argc, char** argv) {
    // Show device availability
    int ndev = 0;
    CHECK(cudaGetDeviceCount(&ndev));
    if (ndev == 0) {
        fprintf(stderr, "No CUDA devices visible. Check CUDA_VISIBLE_DEVICES / node selection.\n");
        return 1;
    }
    int dev = 0;
    CHECK(cudaSetDevice(dev));
    cudaDeviceProp prop{};
    CHECK(cudaGetDeviceProperties(&prop, dev));
    printf("Using device %d: %s (SM %d.%d)\n", dev, prop.name, prop.major, prop.minor);

    unsigned long long iters = 100000000ULL;
    if (argc > 1) iters = strtoull(argv[1], NULL, 10);

    unsigned long long *d_out = nullptr;
    CHECK(cudaMalloc((void**)&d_out, sizeof(unsigned long long)));
    CHECK(cudaMemset(d_out, 0, sizeof(unsigned long long)));

    auto start = std::chrono::high_resolution_clock::now();
    spin_kernel<<<1,1>>>(iters, d_out);
    // Catch launch errors immediately
    CHECK(cudaPeekAtLastError());
    CHECK(cudaDeviceSynchronize());
    auto end = std::chrono::high_resolution_clock::now();

    unsigned long long h_out = 0xDEADBEEFDEADBEEFULL; // sentinel
    CHECK(cudaMemcpy(&h_out, d_out, sizeof(unsigned long long), cudaMemcpyDeviceToHost));
    CHECK(cudaFree(d_out));

    double elapsed = std::chrono::duration<double>(end - start).count();
    printf("Kernel finished. Elapsed time: %.2f seconds\n", elapsed);
    printf("Kernel output: %llu (iters=%llu)\n",
           (unsigned long long)h_out, (unsigned long long)iters);
    return 0;
}

