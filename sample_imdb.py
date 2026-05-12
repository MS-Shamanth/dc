# 3. Textual Classification using IMDB (Movie Review Program)

import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb

# Load IMDB dataset
max_words = 10000

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_words)

# Pad sequences
maxlen = 500

x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# Build model
model = models.Sequential()

# Embedding layer
model.add(
    layers.Embedding(
        input_dim=max_words,
        output_dim=128,
        input_length=maxlen
    )
)

# LSTM layer
model.add(layers.LSTM(64))

# Dense layer
model.add(layers.Dense(64, activation='relu'))

# Output layer
model.add(layers.Dense(1, activation='sigmoid'))

# Display summary
model.summary()

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2
)

# Evaluate model
loss, accuracy = model.evaluate(x_test, y_test)

print(f"\nTest Accuracy: {accuracy:.2f}")

# Predict sample review
prediction = model.predict(x_test[:1])

print("\nPrediction Value:", prediction[0][0])

if prediction[0][0] > 0.5:
    print("Predicted Sentiment: Positive Review")
else:
    print("Predicted Sentiment: Negative Review")
