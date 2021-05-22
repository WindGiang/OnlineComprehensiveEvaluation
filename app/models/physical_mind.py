from typing import TYPE_CHECKING

from sqlalchemy import Float, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class PhysicalMind(Base):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True, index=True)
    activity = Column(Float, nullable=True, comment='自评加分')  # 自评加分
    ext_points = Column(Float, nullable=True, comment='额外加分，最高30')
    deduction_points = Column(Float, nullable=True, comment='扣分项')
    date = Column(Date, nullable=False)
