from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase

from app.models.honor import Honor
from app.schemas.honor import HonorCreate, HonorUpdate


class CRUDHonor(CRUDBase[Honor, HonorCreate, HonorUpdate]):
    def create(self, db: Session, *, obj_in :HonorCreate) -> Any:
        db_obj = Honor(
            student_id=obj_in.student_id,
            type=obj_in.type,
            describe=obj_in.describe,
            classes=obj_in.classes,
            point=obj_in.point,
            date=str(obj_in.date.date())
        )
        db.add(db_obj)
        db.commit()
        return 1


honor = CRUDHonor(Honor)