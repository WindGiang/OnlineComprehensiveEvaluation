from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class AverageGrade(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    grades = Column(Float, nullable=True, comment='平均学分绩')
    grade = Column(Enum('大一', '大二', '大三', '大四', '大五', '大六'), nullable=False, comment='年级', index=True)
