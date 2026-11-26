from app.core.exception import DuplicateStudentError
from app.models.student import Student

class StudentService:
    def __init__(self, store: list[Student]) -> None :
        self.store = store

    def create_student(self, student_item: Student) -> Student:
        if any(True if s.id == student_item.id else False for s in self.store):
            raise DuplicateStudentError
        self.store.append(student_item)
        return student_item

    def get_student(self) -> list[Student]:
        return self.store