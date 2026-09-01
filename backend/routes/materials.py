from fastapi import APIRouter

from database.database import get_connection


router = APIRouter()


@router.get("/api/materials")
def get_materials():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM materials")

    materials = cursor.fetchall()

    connection.close()

    return [dict(material) for material in materials]