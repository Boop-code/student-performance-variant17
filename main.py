
from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from huggingface_hub import hf_hub_download
from pydantic import BaseModel


# Репозиторий с обученной моделью
REPO_ID = "hrip4k/student-performance-variant17"

# Скачивание модели из Hugging Face
model_path = hf_hub_download(
    repo_id=REPO_ID,
    filename="best_model.joblib",
    repo_type="dataset"
)

# Загрузка обученной модели
model = joblib.load(model_path)

# Создание приложения
app = FastAPI(
    title="Student Performance Prediction API",
    description="Сервис прогнозирования успеваемости студентов",
    version="1.0"
)


class StudentData(BaseModel):
    school: str
    sex: str
    age: int
    address: str
    famsize: str
    Pstatus: str
    Medu: int
    Fedu: int
    Mjob: str
    Fjob: str
    reason: str
    guardian: str
    traveltime: int
    studytime: int
    failures: int
    schoolsup: str
    famsup: str
    paid: str
    activities: str
    nursery: str
    higher: str
    internet: str
    romantic: str
    famrel: int
    freetime: int
    goout: int
    Dalc: int
    Walc: int
    health: int
    absences: int
    G1: int
    G2: int


@app.get("/")
def home():
    return {
        "message": "Student Performance API is running"
    }


@app.post("/predict")
def predict(data: StudentData):
    try:
        student = pd.DataFrame([data.model_dump()])
        prediction = model.predict(student)[0]

        return {
            "grade": round(float(prediction), 2)
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )