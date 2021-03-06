import os
import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator, AnyUrl, EmailStr


class Settings(BaseSettings):
    API_V1_STR: str = "/api-dev"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME = "OnlineJudge"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_core_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    MYSQL_SERVER: str = os.getenv('SERVER_ADDR')
    MYSQL_USER: str = os.getenv('SERVER_USER')
    MYSQL_PASSWORD: str = os.getenv('SERVER_PASS')
    MYSQL_DB: str = os.getenv('SERVER_DB')
    SQLALCHEMY_DATABASE_URI: Optional[AnyUrl] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return AnyUrl.build(
            scheme="mysql+pymysql",
            user=values.get("MYSQL_USER"),
            password=values.get("MYSQL_PASSWORD"),
            port="3306",
            host=values.get("MYSQL_SERVER"),
            path=f"/{values.get('MYSQL_DB') or ''}",
            query='charset=utf8mb4'
        )
    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = 'admin@admin.com'
    FIRST_SUPERUSER_PASSWORD: str = 'admin'
    FIRST_SUPERUSER_NAME: str = 'admin'
    FIRST_SUPERUSER_ID: int = 1000
    USERS_OPEN_REGISTRATION: bool = True

    class Config:
        case_sensitive = True


settings = Settings()
