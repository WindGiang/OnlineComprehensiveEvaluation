from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Enum

from sqlalchemy.orm import relationship

from app.db.base_class import Base


class CheckTable(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True, index=True)
    grade = Column(Enum('大一', '大二', '大三', '大四'), nullable=False, comment='年级', index=True)
    honor = Column(Boolean, default=False, comment='荣誉')
    sports_test = Column(Boolean, default=False, comment='体测得分')
    physical_mind = Column(Boolean, default=False, comment='体育和美术')
    moral = Column(Boolean, default=False, comment='品德')
    average_grades = Column(Boolean, default=False, comment='学分绩')
