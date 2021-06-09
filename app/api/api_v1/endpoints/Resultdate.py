from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()

date = {
    'code': 200,
    'data': {
        'tatol': 9,
        'items': [
            {'id': 179074010, 'name': '江丰', 'grades': 80.25, 'academy': '计算机科学与技术学院', 'discipline': '计171',
             'result': '90.1'},
            {'id': 179074011, 'name': '关飞', 'grades': 75.25, 'academy': '计算机科学与技术学院', 'discipline': '计171',
             'result': '89.5'},
            {'id': 179074012, 'name': '余文治', 'grades': 78.12, 'academy': '计算机科学与技术学院', 'discipline': '计172',
             'result': '88.4'},
            {'id': 179074013, 'name': '管杰', 'grades': 80.34, 'academy': '计算机科学与技术学院', 'discipline': '计172',
             'result': '87.1'},
            {'id': 179074014, 'name': '老王', 'grades': 76.26, 'academy': '计算机科学与技术学院', 'discipline': '计173',
             'result': '84.6'},
            {'id': 179074015, 'name': '蒋佳乐', 'grades': 75.45, 'academy': '计算机科学与技术学院', 'discipline': '计173',
             'result': '79.9'},
            {'id': 179074016, 'name': '建国', 'grades': 65.45, 'academy': '计算机科学与技术学院', 'discipline': '计174',
             'result': '78.3'},
            {'id': 179074017, 'name': '小花', 'grades': 56.45, 'academy': '计算机科学与技术学院', 'discipline': '软171',
             'result': '77.4'},
            {'id': 179074018, 'name': '哈哈', 'grades': 60.25, 'academy': '计算机科学与技术学院', 'discipline': '软171',
             'result': '69.1'},

        ]
    }
}


@router.get("/result", response_model=Any)
def result_f() -> Any:
    return date
