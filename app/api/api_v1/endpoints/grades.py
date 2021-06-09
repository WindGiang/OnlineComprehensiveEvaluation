from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get('/', response_model=List[schemas.Grades])
def read_grades(
        db: Session = Depends(deps.get_db),
        current_stu: models.Student = Depends(deps.get_current_student)
) -> Any:
    grades = crud.grades.get_multi_by_stu(db, stu_id=current_stu.id)
    print(grades)

    return grades


