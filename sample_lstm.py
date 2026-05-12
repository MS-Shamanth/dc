import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

data = pd.read_csv("AirPassengers.csv")
dataset = data[["#Passengers"]].values

scaler = MinMaxScaler()
dataset = scaler.fit_transform(dataset)

x = []
y = []

for i in range(5, len(dataset)):
    x.append(dataset[i-5:i, 0])
    y.append(dataset[i, 0])

x = np.array(x)
y = np.array(y)

x = x.reshape(x.shape[0], x.shape[1], 1)

model = Sequential()
model.add(LSTM(50, input_shape=(5, 1)))
model.add(Dense(1))

model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

model.fit(
    x,
    y,
    epochs=20,
    batch_size=1
)

predicted = model.predict(x)
predicted = scaler.inverse_transform(predicted)
original = scaler.inverse_transform(dataset[5:])

plt.plot(original, label='Original')
plt.plot(predicted, label='Predicted')
plt.legend()
plt.show()
