#schemas verification

from typing import Dict, Any
# pyrefly: ignore [missing-import]
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    disease: str
    features: Dict[str, int | float | str] #key--> string format, value can be integer or float


class PredictionResponse(BaseModel):
    disease: str
    prediction: int
    probability: float


class HealthResponse(BaseModel):
    message: str
    status: str



