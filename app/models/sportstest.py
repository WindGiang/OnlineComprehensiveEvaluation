from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Float, Sequence
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Sportstest(Base):
    id = Column(Integer, Sequence('test_seq_id'), primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    grades = Column(Float, nullable=False, comment='得分')
    date = Column(Date, nullable=False)
