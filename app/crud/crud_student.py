import datetime
from typing import Any, Dict, Optional, Union

from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import date

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.academy import Academy
from app.models.student import Student
from app.schemas.student import StudentUpdate, StudentCreate
from app.crud.crud_academy import CRUDAcademy


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def get_by_id(self, db: Session, id: int) -> Student:
        # return db.execute(select(Student, Academy).where(Student.id == id, Academy.id == Student.discipline_id))
        return db.query(Student).filter(Student.id == id).first()

    def get_info(self, db: Session, ):
        pass

    def create(self, db: Session, *, obj_in: StudentCreate) -> Student:
        disciline = db.query(Academy).filter(Academy.discipline_name == obj_in.discipline).first()
        graduate_time = obj_in.admission_time + datetime.timedelta(days=1399)
        db_obj = Student(
            id=obj_in.id,
            name=obj_in.name,
            political_status=obj_in.political_status,
            gender=obj_in.gender,
            phone_number=obj_in.phone_number,
            first_academy=disciline,
            hashed_password=get_password_hash(obj_in.password),
            admission_time=obj_in.admission_time,
            graduate_time=graduate_time,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self,
            db: Session,
            *,
            db_obj: Student,
            obj_in: Union[StudentUpdate, Dict[str, Any]]
    ) -> Student:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get('password'):
            hashed_password = get_password_hash(update_data['password'])
            del update_data['password']
            update_data['hashed_password'] = hashed_password
        if update_data.get('discipline'):
            update_data['first_academy'] = update_data['discipline']
            del update_data['discipline']
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, sid: int, password: str) -> Optional[Student]:
        student = self.get_by_id(db, id=sid)
        if not student:
            return None
        if not verify_password(password, student.hashed_password):
            return None
        return student


student = CRUDStudent(Student)
