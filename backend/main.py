from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.materials import router as materials_router
from routes.processes import router as processes_router
from routes.calculate import router as calculate_router
from routes.predict import router as predict_router
from database.database import initialize_database


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://idp-project-gamma.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
initialize_database()


@app.get("/")
def home():
    return {
        "message": "Composite Materials Engineering Platform Backend is running!"
    }


app.include_router(materials_router)
app.include_router(processes_router)
app.include_router(calculate_router)
app.include_router(predict_router)