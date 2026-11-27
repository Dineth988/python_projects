from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.student import StudentCreate, StudentResponse
from app.services import student_service


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

DbDependency = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    db: DbDependency
):
    return student_service.create_student(db, student)


@router.get("/", response_model=list[StudentResponse])
def get_students(db: DbDependency):
    return student_service.get_students(db)

@router.get("/{id}", response_model=StudentResponse)
def get_student_by_id(db: DbDependency, id: int):
    return student_service.get_student_by_id(db, id)

@router.delete("/{id}", response_model=StudentResponse)
def delete_student_by_id(db: DbDependency, id: int):
    return student_service.delete_student(db, id)