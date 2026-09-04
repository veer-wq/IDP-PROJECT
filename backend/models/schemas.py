from pydantic import BaseModel


class CalculationInput(BaseModel):
    length: float
    width: float
    thickness: float
    density: float


class PredictionInput(BaseModel):
    fiber_type: str
    resin_type: str
    fiber_volume_fraction: float
    manufacturing_process: str