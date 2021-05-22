from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Honor(Base):
    id = Column(Integer, index=True, nullable=False, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), index=True, primary_key=True)
    type = Column(Enum('奖学金', '竞赛', '荣誉称号'), nullable=False, index=True)
    describe = Column(String(100), nullable=False, index=True)
    classes = Column(Enum('思想品德', '学业', '文体'))
    point = Column(Integer, nullable=True)
    is_check = Column(Enum('通过', '未通过', '待审核'), default='待审核')
    date = Column(Date, nullable=False)
