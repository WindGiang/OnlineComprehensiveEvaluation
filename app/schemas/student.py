from datetime import date

from typing import Optional

from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    phone_number: Optional[str] = None
    name: Optional[str] = None


class StudentUpdate(StudentBase):
    password: Optional[str] = None
    discipline: Optional[str] = None
    graduate_time: Optional[date] = None


class StudentInDBBase(StudentBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class StudentCreate(StudentBase):
    id: int
    name: str
    password: str
    phone_number: str
    discipline: str
    discipline_second: Optional[str] = None
    gender: str
    admission_time: date


class Student(StudentInDBBase):
    pass


class StudentInDB(StudentInDBBase):
    hashed_password: str
