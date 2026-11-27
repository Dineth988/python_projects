
from fastapi import FastAPI

from app.core.config import APP_NAME, APP_VERSION
from app.api.students import router as student_router
from app.db.database import Base, engine
from app.db import models

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(student_router)


@app.get("/")
def root():
    return {"message": "Student API is running"}
