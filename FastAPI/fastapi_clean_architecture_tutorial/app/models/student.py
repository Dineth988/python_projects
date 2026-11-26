from pydantic import BaseModel, Field
from typing import Annotated

class Student(BaseModel):
    s_id: int
    name: Annotated[str, Field(min_length=3, max_length=50)]
    age: Annotated[int, Field(gt=0, lt=100)]