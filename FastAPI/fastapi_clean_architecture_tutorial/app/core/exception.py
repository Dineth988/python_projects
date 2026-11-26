# app/core/exceptions.py
class DuplicateStudentError(Exception):
    def __init__(self, s_id: int) -> None:
        self.message = f"Student with s_id {s_id} already exists"
        super().__init__(self.message)