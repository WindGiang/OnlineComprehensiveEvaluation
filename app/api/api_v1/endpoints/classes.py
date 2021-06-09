from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.post("/create", response_model=schemas.Classes)
def create_classes(
        *,
        db: Session = Depends(deps.get_db),
        classes_in: schemas.ClassesCreate,
) -> Any:
    classes = crud.classes.create(db, obj_in=classes_in)
    return classes


@router.get('/all', response_model=List[schemas.Classes])
def get_classes(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    classes = crud.classes.get_multi(db, skip=skip, limit=limit)
    return classes
