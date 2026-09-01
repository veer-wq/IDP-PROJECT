from fastapi import APIRouter

from models.schemas import CalculationInput


router = APIRouter()


@router.post("/api/calculate")
def calculate(data: CalculationInput):

    length_m = data.length / 1000
    width_m = data.width / 1000
    thickness_m = data.thickness / 1000

    volume = length_m * width_m * thickness_m

    mass = volume * data.density

    return {
        "volume": volume,
        "volume_unit": "m3",
        "mass": mass,
        "mass_unit": "kg"
    }