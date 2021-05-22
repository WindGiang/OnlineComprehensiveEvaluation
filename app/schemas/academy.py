from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class AcademyBase(BaseModel):
    academy_name: Optional[str] = None
    discipline_name: Optional[str] = None


# Properties to receive via API on creation
class AcademyCreate(AcademyBase):
    discipline_name: str
    academy_name: str


# Properties to receive via API on update
class AcademyUpdate(AcademyBase):
    discipline_name: Optional[str] = None
    academy_name: Optional[str] = None


class AcademyInDBBase(AcademyBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Academy(AcademyInDBBase):
    pass


# Additional properties stored in DB
class AcademyInDB(AcademyInDBBase):
    discipline: str
