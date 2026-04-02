import joblib
import numpy as np

# load trained model (we will add later)
model = joblib.load("crop_model.pkl")

def predict_crop(soil, season, water):
    input_data = np.array([[soil, season, water]])
    prediction = model.predict(input_data)
    return prediction[0]