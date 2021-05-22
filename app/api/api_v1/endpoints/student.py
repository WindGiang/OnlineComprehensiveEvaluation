from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/{student_id}", response_model=schemas.Student)
def read_student(
        student_id: int,
        db: Session = Depends(deps.get_db),

) -> Any:
    student = crud.student.get(db, id=student_id)
    return student


@router.post('/', response_model=schemas.Student)
def create_student(
      *,
      db: Session = Depends(deps.get_db),
      student_in: schemas.StudentCreate,
) -> Any:
    student = crud.student.get_by_id(db, id=student_in.id)
    if student:
        raise HTTPException(
            status_code=400,
            detail='当前学生已存在',
        )
    student = crud.student.create(db, obj_in=student_in)

    return student
