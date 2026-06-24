#include <cuda_runtime.h>

__global__ void leaky_relu_kernel(const float* input, float* output, float alpha, int N) {
    // Write code here
    int i = threadIdx.x + blockDim.x * blockIdx.x;

    if(i>N-1){
        return;
    }

    output[i] = fmaxf(input[i], 0) + alpha * fminf(input[i], 0);
}

extern "C" void solve(const float* input, float* output, float alpha, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    leaky_relu_kernel<<<blocks, threads>>>(input, output, alpha, N);
    cudaDeviceSynchronize();
}