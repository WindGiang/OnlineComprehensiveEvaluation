import enum
from typing import TYPE_CHECKING

from sqlalchemy import Enum, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .academy import Academy  # noqa


class Student(Base):
    id = Column(Integer, unique=True, nullable=False, primary_key=True, index=True, comment='学号')
    name = Column(String(30), index=True, nullable=False)
    gender = Column(Enum('男', '女'))
    political_status = Column(Enum('群众', '团员', '积极分子', '预备党员', '党员'))  # 政治面貌
    phone_number = Column(String(15), index=True)
    discipline_id = Column(Integer, ForeignKey('academy.id'), nullable=False)
    discipline_id_second = Column(Integer, ForeignKey('academy.id'), nullable=True)
    first_academy = relationship('Academy', backref='students_first_academy', foreign_keys=[discipline_id])
    second_academy = relationship('Academy', backref='students_second_academy', foreign_keys=[discipline_id_second])
    hashed_password = Column(String(150), nullable=False)
    admission_time = Column(Date)
    graduate_time = Column(Date)
