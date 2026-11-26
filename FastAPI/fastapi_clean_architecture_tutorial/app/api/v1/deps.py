# app/api/deps.py
from typing import Annotated
from fastapi import Depends
from app.db.memory import get_student_store
from app.models.student import Student
from app.services.student_service import StudentService

StoreDep = Annotated[list[Student], Depends(get_student_store)]


def get_student_service(store: StoreDep) -> StudentService:
    return StudentService(store)


StudentServiceDep = Annotated[StudentService, Depends(get_student_service)]