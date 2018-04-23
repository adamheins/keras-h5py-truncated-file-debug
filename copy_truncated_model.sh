#!/bin/bash

# Create the keras models directory if it doesn't exist.
mkdir -p ~/.keras/models

# Copy in our intentionally truncated file to simulate an interrupted download.
cp vgg16_weights_tf_dim_ordering_tf_kernels_truncated.h5 ~/.keras/models/vgg16_weights_tf_dim_ordering_tf_kernels.h5
