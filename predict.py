import pandas as pd
import joblib

model = joblib.load("models/heart_model.pkl")
scaler = joblib.load("models/scaler.pkl")

columns = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach",
    "exang", "oldpeak", "slope",
    "ca", "thal"
]

def predict_heart_risk(features):
    df = pd.DataFrame([features], columns=columns)

    scaled = scaler.transform(df)

    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]

    return prediction, probability