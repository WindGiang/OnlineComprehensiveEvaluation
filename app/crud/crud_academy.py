from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.academy import Academy
from app.schemas.academy import AcademyCreate, AcademyUpdate


class CRUDAcademy(CRUDBase[Academy, AcademyCreate, AcademyUpdate]):
    def get_discipline_id_by_name(self, db: Session, *, name: str) -> Optional[str]:
        return db.query(Academy).filter(Academy.discipline_name == name).first()


academy = CRUDAcademy(Academy)
