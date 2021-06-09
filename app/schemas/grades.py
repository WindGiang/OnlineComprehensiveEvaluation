from typing import Optional

from pydantic import BaseModel


class GradesBase(BaseModel):
    class_id: int
    student_id: int
    grade: float


class GradeCreate(GradesBase):
    pass


class GradeUpdate(GradesBase):
    pass


class GradesInDB(GradesBase):
    class_id: Optional[int] = None
    student_id: Optional[int] = None

    class Config:
        orm_mode = True


class Grades(BaseModel):
    grade: float
    class_name: str
    credit: float
