from fastapi import APIRouter

from database.database import get_connection


router = APIRouter()


@router.get("/api/processes")
def get_processes():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM processes")

    processes = cursor.fetchall()

    connection.close()

    return [dict(process) for process in processes]