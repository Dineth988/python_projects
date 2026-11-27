from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    age: int = Field(gt=0)

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int

class StudentUpdate(BaseModel):
    name: str | None
    age: int | None