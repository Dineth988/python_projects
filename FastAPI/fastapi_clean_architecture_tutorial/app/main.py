# from fastapi import FastAPI


# students: list[Student] = []

# app = FastAPI(title="Clean Architecture")


# @app.post("/students")
# async def create_student(student_item: Student):
#     students.append(student_item)
#     return student_item

# @app.get("/students")
# async def get_students():
#     return students

# app/main.py
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.exception import DuplicateStudentError

settings = get_settings()
app = FastAPI(title=settings.app_title)


@app.exception_handler(DuplicateStudentError)
async def duplicate_student_handler(_: Request, exc: DuplicateStudentError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": exc.message},
    )


app.include_router(api_router)