from typing import Any, Dict, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.sportstest import Sportstest
from app.schemas.sportstest import SportstestCreat, SportstestUpdate

class CRUDSportstest(CRUDBase[Sportstest, SportstestCreat, SportstestUpdate]):
    def create(self, db: Session, *, obj_in: SportstestCreat) -> int:
        db_obj = Sportstest(
            student_id=obj_in.student_id,
            grades=obj_in.grades,
            date=obj_in.date
        )
        db.add(db_obj)
        db.commit()
        return 1


sportstest = CRUDSportstest(Sportstest)