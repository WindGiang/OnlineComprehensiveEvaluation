from pydantic import BaseModel
from datetime import datetime

class HonorBase(BaseModel):
    student_id: int
    type: str
    describe: str
    classes: str
    point: float
    date: datetime

class HonorCreate(HonorBase):
    pass

class HonorUpdate(HonorBase):
    pass


class Honor(HonorBase):
    class Config:
        orm_mode = True