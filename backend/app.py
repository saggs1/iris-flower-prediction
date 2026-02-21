from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import os
import numpy as np

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model & scaler
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR,"..","model","model.pkl")
SCALER_PATH = os.path.join(BASE_DIR,"..","model","scaler.pkl")                        
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Target names
classes = ["Setosa", "Versicolor", "Virginica"]

@app.get("/")
def home():
    return {"message": "Iris Prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    
    features = np.array([
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]).reshape(1, -1)

    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)

    return {
        "prediction": classes[prediction[0]]
    }