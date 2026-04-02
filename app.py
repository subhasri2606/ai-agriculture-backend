from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    soil = data["soil"]
    season = data["season"]
    water = data["water"]

    # 🌱 SIMPLE REAL LOGIC (no ML model needed)
    if soil == 0 and water == 2:
        crop = "Rice"
    elif soil == 1 and season == 1:
        crop = "Wheat"
    elif soil == 2 and water == 0:
        crop = "Millets"
    else:
        crop = "Maize"

    return jsonify({
        "recommended_crop": crop,
        "confidence": 85,
        "note": "Rule-based recommendation system"
    })

@app.route("/predict", methods=["POST"])
def predict():
    import random
    import numpy as np

    data = request.get_json()

    crop = data.get("crop", "Rice")
    days = int(data.get("days", 7))

    base_price = np.random.randint(20, 120)

    forecast = []
    price = base_price

    for i in range(days):
        change = random.randint(-5, 6)  # up or down movement
        price += change

        forecast.append({
            "day": f"Day {i+1}",
            "price": round(price, 2)
        })

    return jsonify({
        "crop": crop,
        "forecast": forecast,
        "trend": "Fluctuating"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
