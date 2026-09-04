from fastapi import APIRouter
from models.schemas import CalculationInput

router = APIRouter()


@router.post("/api/calculate")
def calculate(data: CalculationInput):

    # Dimensions are already in meters
    length_m = data.length
    width_m = data.width
    thickness_m = data.thickness

    # Calculate volume
    volume = length_m * width_m * thickness_m

    # Calculate mass
    mass = volume * data.density

    return {
        "volume": volume,
        "volume_unit": "m3",
        "mass": mass,
        "mass_unit": "kg"
    }