from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/me", response_model=Any)
def read_stu_me(
        db: Session = Depends(deps.get_db),
        current_stu: models.Student = Depends(deps.get_current_student)
) -> Any:
    stu = jsonable_encoder(current_stu)
    academy = crud.academy.get(db, id=current_stu.discipline_id)
    stu['first_academy'] = academy.discipline_name
    stu['academy'] = academy.academy_name
    del stu['hashed_password']
    return stu


@router.get("/{student_id}", response_model=schemas.Student)
def read_student(
        student_id: int,
        db: Session = Depends(deps.get_db),

) -> Any:
    student = crud.student.get_by_id(db, id=student_id)
    return student


@router.post('/create', response_model=schemas.Student)
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


@router.post('/creatmulti', response_model=Any)
def creat_mutil_stu(
        *,
        db: Session = Depends(deps.get_db),
        student_in: List[schemas.StudentCreate]
) -> Any:
    count = 0
    stulist = []
    for item in student_in:
        print(item)
        stu = crud.student.get_by_id(db, id=item.id)
        if stu:
           stulist.append(item.id)
        if not stu:
            count += 1
            stu = crud.student.create(db, obj_in=item)
    print(stulist,count)
    return {'message':'成功创建'+str(count)+'位学生'+'其中'+str(stulist)+'未创建'}


@router.put('/update', response_model=schemas.Msg)
def update_student(
        *,
        db: Session = Depends(deps.get_db),
        student_in: schemas.StudentUpdate
) -> Any:
    student = crud.student.get_by_id(db, id=student_in.id)
    if not student:
        raise HTTPException(
            status_code=404,
            detail='学生不存在'
        )
    student = crud.student.update(db, db_obj=student, obj_in=student_in)
    return {'msg': 'update successful'}
