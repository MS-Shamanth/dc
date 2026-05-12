# 2.Autoencoders & Decoders

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Reshape

# Load MNIST dataset
(x_train, _), (x_test, _) = mnist.load_data()

# Normalize data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build Autoencoder Model
model = Sequential([

    # Convert 28x28 image into 784 vector
    Flatten(input_shape=(28, 28)),

    # Encoder layer (Compression)
    Dense(64, activation='relu'),

    # Decoder layer (Reconstruction)
    Dense(784, activation='sigmoid'),

    # Convert back to 28x28 image
    Reshape((28, 28))
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy'
)

# Train model
model.fit(
    x_train,
    x_train,
    epochs=5,
    batch_size=256
)

# Reconstruct images
decoded_images = model.predict(x_test)

# Display results
n = 5

plt.figure(figsize=(10, 4))

for i in range(n):

    # Original image
    plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i], cmap='gray')
    plt.title("Original")
    plt.axis('off')

    # Reconstructed image
    plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_images[i], cmap='gray')
    plt.title("Output")
    plt.axis('off')

plt.show()
