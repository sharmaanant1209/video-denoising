The network had thirteen layers:
1. Convolutional layer: 3 × 3 kernel with 70 filters
2. Max pooling layer: stride of two
3. Convolutional layer: 3 × 3 kernel with 60 filters
4. Max pooling later: stride of two
5. Convolutional layer: 3 × 3 kernel with 50 filters
6. Max pooling later: stride of two
7. Convolutional layer: 3 × 3 kernel with 50 filters
8. Upscaling layer: scale factor of two
9. Convolutional layer: 3 × 3 kernel with 60 filters
10. Upscaling layer: scale factor of two
11. Convolutional layer: 3 × 3 kernel with 70 filters
12. Upscaling layer: scale factor of two
13. Convolutional layer: 3 × 3 kernel with one filter
All layers used a rectified linear unit (ReLU) activation
function except for the last, which used a sigmoid activation.
hi
