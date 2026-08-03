from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load only model
model = joblib.load("lightgbm_model.pkl")


@app.get("/")
def home():
    return {"message": "Loan Default API running inside Docker"}


@app.post("/predict")
def predict(data: dict):

    sk_id = data["sk_id_curr"]

    # ❌ REMOVE dataset usage
    # Instead assume input features come from request

    features = data["features"]  # list of feature values

    X = pd.DataFrame([features])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    return {
        "sk_id_curr": sk_id,
        "prediction": int(pred),
        "probability": float(prob)
    }