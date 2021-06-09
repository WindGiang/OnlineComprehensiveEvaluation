from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.post('/createhonor', response_model=Any)
def create_Honor(
        *,
        db: Session = Depends(deps.get_db),
        honor_in: schemas.HonorCreate
) -> Any:
    issuccess = crud.honor.create(db, obj_in=honor_in)
    return {
        'code': 200,
        'message': '创建成功，请等待审核'
    }
