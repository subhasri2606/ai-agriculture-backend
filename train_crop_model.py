import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 🌾 SIMPLE TRAINED MODEL (NO FILE NEEDED)
X = np.array([
    [0,0,0],
    [0,1,1],
    [1,1,1],
    [2,2,2],
    [1,2,1],
    [2,1,2]
])

y = np.array([
    "Rice",
    "Wheat",
    "Maize",
    "Sugarcane",
    "Rice",
    "Cotton"
])

crop_model = RandomForestClassifier()
crop_model.fit(X, y)