from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib
import numpy as np
import os

app = FastAPI(title="Diabetes Model API")

# Load trained model
MODEL_PATH = "app/models/diabetes_rf_model.joblib"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model not found at {MODEL_PATH}. Run train_model.py first."
    )

model = joblib.load(MODEL_PATH)

# Diabetes dataset has 10 features
NUM_FEATURES = 10

# Pydantic model for request validation
class PredictionRequest(BaseModel):
    features: conlist(float, min_length=NUM_FEATURES, max_length=NUM_FEATURES)

# Root route: health check
@app.get("/")
def health_check():
    return {"status": "ok", "message": "Diabetes prediction API is running!"}

# Prediction route
@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        # Convert input features to numpy array
        X = np.array(request.features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(X)[0]

        return {"prediction": float(prediction)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
