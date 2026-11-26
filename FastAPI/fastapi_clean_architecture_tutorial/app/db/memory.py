from app.models.student import Student

_students_store: list[Student] = []

def get_student_store() -> list[Student]:
    return _students_store