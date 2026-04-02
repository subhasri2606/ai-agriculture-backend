import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import joblib

# LOAD DATA
df = pd.read_csv("priceagriculture.csv")
df.columns = df.columns.str.strip()

df["Arrival_Date"] = pd.to_datetime(df["Arrival_Date"], errors="coerce")
df = df.dropna(subset=["Arrival_Date", "Modal Price", "Commodity"])

# SELECT ONE COMMODITY
commodity = "Tomato"

data = df[df["Commodity"] == commodity].copy()
data = data.sort_values("Arrival_Date")

prices = data["Modal Price"].values.reshape(-1, 1)

# SCALE
scaler = MinMaxScaler()
scaled = scaler.fit_transform(prices)

# ✅ SAVE SCALER (AFTER FITTING)
joblib.dump(scaler, "scaler.pkl")

# CREATE SEQUENCE
def create_dataset(dataset, step=5):
    X, y = [], []
    for i in range(len(dataset) - step):
        X.append(dataset[i:i+step, 0])
        y.append(dataset[i+step, 0])
    return np.array(X), np.array(y)

step = 5
X, y = create_dataset(scaled, step)

X = X.reshape(X.shape[0], X.shape[1], 1)

# MODEL
model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(step, 1)),
    LSTM(64),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")

# TRAIN
model.fit(X, y, epochs=15, batch_size=16)

# SAVE MODEL
model.save("price_lstm_model.h5")

print("✅ Model + Scaler saved successfully!")