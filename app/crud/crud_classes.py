from typing import Any, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.classes import Classes
from app.schemas.classes import ClassesCreate, ClassesUpdate


class CRUDClasses(CRUDBase[Classes, ClassesCreate, ClassesUpdate]):
    def create(self, db: Session, *, obj_in: ClassesCreate) -> Any:
        db_obj = Classes(
            class_name=obj_in.class_name,
            type=obj_in.type,
            credit=obj_in.credit,
            hour=obj_in.hour
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Classes]:
        classes=db.query(Classes).limit(limit).all()
        return classes


classes = CRUDClasses(Classes)
