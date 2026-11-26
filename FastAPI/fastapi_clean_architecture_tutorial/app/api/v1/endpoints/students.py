# app/api/endpoints/students.py
from fastapi import APIRouter, status
from app.api.v1.deps import StudentServiceDep
from app.models.student import Student

router = APIRouter(prefix="/students", tags=["students"])


@router.post("", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(student_item: Student, service: StudentServiceDep) -> Student:
    return service.create_student(student_item)


@router.get("", response_model=list[Student])
async def get_students(service: StudentServiceDep) -> list[Student]:
    return service.get_students()