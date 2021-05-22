from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            full_name=settings.FIRST_SUPERUSER_NAME,
            id=settings.FIRST_SUPERUSER_ID
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
    academy = crud.academy.get_discipline_id_by_name(db, name='计算机科学与技术')
    if not academy:
        academy_in = schemas.AcademyCreate(
            academy_name='计算机科学与技术学院',
            discipline_name='计算机科学与技术'
        )
        academy = crud.academy.create(db, obj_in=academy_in)
        academy_in = schemas.AcademyCreate(
            academy_name='计算机科学与技术学院',
            discipline_name='软件工程'
        )
        academy = crud.academy.create(db, obj_in=academy_in)
