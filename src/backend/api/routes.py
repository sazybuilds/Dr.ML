# pyrefly: ignore [missing-import]
from fastapi import APIRouter

from src.backend.schemas.prediction_schema import (
    PredictionRequest,
    PredictionResponse,
    HealthResponse
)

from src.backend.services.predictor import predict_disease


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "okay",
        "message": "API is healthy and running"
    }


@router.post("/predict", response_model=PredictionResponse)
def predict_endpoint(request: PredictionRequest):
    disease = request.disease
    features = request.features
    result = predict_disease(disease, features)
    return PredictionResponse(**result)