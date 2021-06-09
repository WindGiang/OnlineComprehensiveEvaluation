from typing import Any, List

from sqlalchemy.orm import Session

from app import schemas
from app.crud.base import CRUDBase
from app.models import Student, Classes
from app.models.grades import Grades
from app.schemas.grades import GradeCreate, GradeUpdate


class CRUDGrades(CRUDBase[Grades, GradeUpdate, GradeCreate]):
    def get_multi_by_stu(
        self, db: Session, *, stu_id: int,
    ) -> List[schemas.Grades]:
        grade = db.query(Grades.grade, Classes.class_name, Classes.credit).filter(Grades.student_id == stu_id, Classes.id == Grades.class_id).all()
        print(grade)
        return grade


grades = CRUDGrades(Grades)
