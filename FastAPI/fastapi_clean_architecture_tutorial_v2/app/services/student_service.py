from app.models.student import StudentResponse, StudentCreate
import app.db.database as db
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models import Student as StudentDB
from sqlalchemy import select, delete


def create_student(db: Session, student: StudentCreate):
    new_student = StudentDB(
        name = student.name, 
        age = student.age
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


def get_students(db: Session):
    statement = select(StudentDB)
    return db.scalars(statement).all()

def get_student_by_id(db: Session, id: int):
    statement = select(StudentDB).where(StudentDB.id == id)
    return db.scalar(statement)

def delete_student(db: Session, id: int):
    statement = select(StudentDB).where(StudentDB.id == id)
    student =  db.scalar(statement)
    db.delete(student)
    db.commit()
    return student
   