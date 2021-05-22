from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Moral(Base):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True, index=True)
    political_status = Column(Integer)  # 政治面貌
    keep_law = Column(Integer)  # 纪律观念
    collective_honor = Column(Integer)  # 集体观念
    self_cultivation = Column(Integer, comment='基础文明修养')  # 基础文明修养
    dormitory_honor = Column(Integer, comment='寝室文明')  # 寝室文明
    social_practice = Column(Integer, comment='社会实践')  # 社会实践
    extra_points = Column(Integer, comment='额外加分')  # 额外加分
    deduction_points = Column(Integer, nullable=True, comment='扣分项')
    date = Column(Date)  # 学年
