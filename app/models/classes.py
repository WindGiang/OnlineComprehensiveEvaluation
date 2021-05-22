from typing import TYPE_CHECKING

from sqlalchemy import Enum, Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Classes(Base):
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(50), index=True, nullable=False)
    type = Column(Enum('必修课', '选修课'), nullable=False)  # 必修课 or 选修课 or 公共选修课
    credit = Column(Float, nullable=False)  # 学分
    hour = Column(Integer, nullable=False, comment='学时')  # 课时
