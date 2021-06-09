from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()

@router.post('/Createmulti', response_model=Any)
def create_sportstest(
        *,
        db: Session = Depends(deps.get_db),
        STGrade_in: List[schemas.SportstestCreat]
) -> Any:
    count = 0
    for item in STGrade_in:
        count += crud.sportstest.create(db, obj_in=item)
    return {'code': 200, 'message': '创建了'+str(count)+'条成绩'}
