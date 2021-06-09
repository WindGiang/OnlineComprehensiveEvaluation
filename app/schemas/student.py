import enum
from datetime import date

from typing import Optional

from pydantic import BaseModel


class Political(str, enum.Enum):
    dangyuan = '党员'
    yubei = '预备党员'
    jijiifenzi = '积极份子'
    tuanyaun = '团员'
    qunzhong = '群众'


class Gender(str, enum.Enum):
    male = '男'
    female = '女'


class StudentBase(BaseModel):
    id: int
    name: Optional[str] = None


class StudentUpdate(StudentBase):
    password: Optional[str] = None
    discipline: Optional[str] = None
    graduate_time: Optional[date] = None
    political_status: Optional[Political] = None


class StudentInDBBase(StudentBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class StudentCreate(StudentBase):
    name: str
    password: str
    political_status: Optional[Political] = None
    discipline: str
    discipline_second: Optional[str] = None
    phone_number: Optional[str] = None
    gender: Gender
    admission_time: date


class Student(StudentInDBBase):
    pass


class StudentInDB(StudentInDBBase):
    hashed_password: str
