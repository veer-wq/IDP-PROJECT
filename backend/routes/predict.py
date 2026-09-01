from fastapi import APIRouter

from models.schemas import PredictionInput


router = APIRouter()


@router.post("/api/predict")
def predict(data: PredictionInput):

    return {
        "prediction": 750,
        "unit": "MPa",
        "message": "Placeholder prediction - ML model will be integrated later"
    }