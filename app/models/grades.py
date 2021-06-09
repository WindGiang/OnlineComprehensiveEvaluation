from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Grades(Base):
    class_id = Column(Integer, ForeignKey('classes.id'), index=True, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), index=True, primary_key=True)
    class_name = relationship('Classes')
    student = relationship('Student')
    grade = Column(Float, nullable=False)  # 成绩
