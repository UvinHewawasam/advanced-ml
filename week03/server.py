from pathlib import Path
import typing as Literal

import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "mlr_mpg_v1.joblib"

app = FastAPI(title="MPG Linear Regression Model API", 
              description="A FastAPI application for predicting MPG using a linear regression model.",
              version="1.0.0"
              )


class PredictionRequest(BaseModel):
    # cylinders: Literal.Optional[int] = Field(..., description="Number of cylinders in the engine")
    displacement: float = Field(..., description="Engine displacement in cubic inches")
    horsepower: float = Field(..., description="Engine horsepower")
    weight: float = Field(..., description="Vehicle weight in pounds")
    acceleration: float = Field(..., description="Time taken to accelerate from 0 to 60 mph in seconds")
    model_year: int = Field(..., description="Model year of the vehicle")
    origin: int = Field(..., description="Origin of the vehicle (1=USA, 2=Europe, 3=Japan)")


class PredictionResponse(BaseModel):
    predicted_mpg: float = Field(..., description="Predicted miles per gallon (MPG)")


class load_model():
    def __init__(self, model_path: Path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        return joblib.load(self.model_path)

try:
    model_loader = load_model(MODEL_PATH)
    # model = model_loader.model
except Exception as e:
    raise RuntimeError(f"Failed to load the model: {e}")
else:
    model_load_error = None
    # model = model_loader.model


def build_inference_frame(request_data: PredictionRequest) -> pd.DataFrame:
    # return pd.DataFrame([request_data.model_dump()])
    return pd.DataFrame([{
        "displacement": request_data.displacement,
        "horsepower": request_data.horsepower,
        "weight": request_data.weight,
        "acceleration": request_data.acceleration,
        "model year": request_data.model_year,
        "origin": request_data.origin,
    }])


@app.post("/predict", response_model=PredictionResponse)
def predict(request_data: PredictionRequest):
    if model_load_error:
        raise HTTPException(status_code=500, detail=f"Model loading error: {model_load_error}")

    try:
        inference_frame = build_inference_frame(request_data)
        predicted_mpg = model_loader.model.predict(inference_frame)[0]
        return PredictionResponse(predicted_mpg=predicted_mpg)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")


@app.get("/health", response_model=dict)
def health_check():
    return {"status": "ok", "model_loaded": MODEL_PATH.name}
