import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Reshape

(x_train, _), (x_test, _) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(64, activation='relu'),
    Dense(784, activation='sigmoid'),
    Reshape((28, 28))
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy'
)

model.fit(
    x_train,
    x_train,
    epochs=5,
    batch_size=256
)

decoded_images = model.predict(x_test)

n = 5
plt.figure(figsize=(10, 4))

for i in range(n):
    plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i], cmap='gray')
    plt.title("Original")
    plt.axis('off')

    plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_images[i], cmap='gray')
    plt.title("Output")
    plt.axis('off')

plt.show()
