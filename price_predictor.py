import numpy as np
from keras.models import load_model
import joblib

model = load_model("price_lstm_model.h5", compile=False)

# load scaler (we must save it during training)
scaler = joblib.load("scaler.pkl")

def predict_price(last_prices):

    seq = np.array(last_prices).reshape(-1, 1)

    # scale input
    seq_scaled = scaler.transform(seq)

    seq_scaled = seq_scaled.reshape(1, seq_scaled.shape[0], 1)

    pred = model.predict(seq_scaled)

    # inverse transform
    real_price = scaler.inverse_transform(pred)

    return float(real_price[0][0])