import enum
from typing import Optional

from pydantic import BaseModel


class CType(str, enum.Enum):
    Compulsory_course = '必修课'
    Elective_course = '选修课'


class ClassesBase(BaseModel):
    type: Optional[CType]
    credit: Optional[float]
    hour: Optional[int]
    class_name: Optional[str]


class ClassesCreate(ClassesBase):
    type: CType
    credit: float
    hour: int
    class_name: str


class ClassesUpdate(ClassesBase):
    pass


class ClassesInDB(ClassesBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class Classes(ClassesInDB):
    pass
