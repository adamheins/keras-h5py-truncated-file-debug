#!/usr/bin/env python
from __future__ import print_function

import numpy as np
from keras.applications import vgg16
from keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions

# Create the VGG model. This downloads the imagenet weights into
# ~/.keras/models and is the source of our problems.
model = vgg16.VGG16(weights='imagenet', include_top=True)

# Load the image to run through the VGG model.
img_path = 'cat.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = vgg16.preprocess_input(x)

# Run the image through the model.
preds = model.predict(x)

label = decode_predictions(preds)
print(label)
