from datetime import date
from typing import Optional

from pydantic import BaseModel


class SportstestBase(BaseModel):
    student_id: int
    grades: float
    date: date

class SportstestCreat(SportstestBase):
    pass

class SportstestUpdate(SportstestBase):
    grades: Optional[float]
    date: Optional[date]

class Sportstest(SportstestBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

