from fastapi import APIRouter

from app.api.api_v1.endpoints import users, login, student, classes, grades, sportstest, Resultdate
from app.api.api_v1.endpoints import honor
api_router = APIRouter()
api_router.include_router(login.router, tags=["登陆相关"])
api_router.include_router(users.router, prefix="/users", tags=["用户相关"])
api_router.include_router(student.router, prefix="/student", tags=['学生相关'])
api_router.include_router(classes.router, prefix="/classes", tags=['课程相关'])
api_router.include_router(grades.router, prefix="/grades", tags=['学分成绩相关'])
api_router.include_router(sportstest.router, prefix='/sportstest', tags=['体测'])
api_router.include_router(Resultdate.router, prefix='/r', tags=['结果获取'])
api_router.include_router(honor.router, prefix='/honor', tags=['荣誉接口'])
