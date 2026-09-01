from pydantic import BaseModel


class CalculationInput(BaseModel):
    length: float
    width: float
    thickness: float
    density: float


class PredictionInput(BaseModel):
    length: float
    width: float
    thickness: float
    density: float