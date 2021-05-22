from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Academy(Base):
    id = Column(Integer, primary_key=True, index=True)
    academy_name = Column(String(30), index=True, nullable=False)  # 学院
    discipline_name = Column(String(30), index=True, nullable=False)  # 专业名称
    # students = relationship('Student', back_populates='stu_academy', foreign_keys=id)
    # students_second = relationship('Student', back_populates='stu_academy_second', foreign_keys=id)
