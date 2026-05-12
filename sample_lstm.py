# 4.LSTM Forecasting

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load dataset
data = pd.read_csv("AirPassengers.csv")

# Select passenger column
dataset = data[["#Passengers"]].values

# Normalize data
scaler = MinMaxScaler()

dataset = scaler.fit_transform(dataset)

# Create input and output
x = []
y = []

for i in range(5, len(dataset)):
    x.append(dataset[i-5:i, 0])
    y.append(dataset[i, 0])

x = np.array(x)
y = np.array(y)

# Reshape for LSTM
x = x.reshape(x.shape[0], x.shape[1], 1)

# Build model
model = Sequential()

model.add(LSTM(50, input_shape=(5, 1)))

model.add(Dense(1))

# Compile model
model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

# Train model
model.fit(
    x,
    y,
    epochs=20,
    batch_size=1
)

# Predict values
predicted = model.predict(x)

# Convert back to original values
predicted = scaler.inverse_transform(predicted)

original = scaler.inverse_transform(dataset[5:])

# Plot graph
plt.plot(original, label='Original')
plt.plot(predicted, label='Predicted')

plt.legend()

plt.show()
