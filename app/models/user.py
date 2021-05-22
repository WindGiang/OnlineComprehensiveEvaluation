from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True, comment='老师的工号')
    full_name = Column(String(20), index=True)
    phone_number = Column(String(15), index=True, nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    prof = Column(String(20), nullable=True, comment='老师的职称')
    hashed_password = Column(String(200), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False, comment='False为老师，True为超级管理员')
    gender = Column(Enum('男', '女'), nullable=True, default='男')
