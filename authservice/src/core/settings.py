import logging
from logging import config as logging_config
from dotenv import load_dotenv

from pydantic_settings import BaseSettings
from sqlalchemy import URL

from core.logger import LOGGING

load_dotenv()

logging_config.dictConfig(LOGGING)

logger = logging.getLogger("AuthService")


class MyConfig(BaseSettings):
    project_name: str = "auth"

    auth_host: str = "localhost"
    auth_port: int = 8000

    postgres_host: str = "127.0.0.45"
    postgres_port: int = 5432

    postgres_db_auth: str = "POSTGRES_DB_AUTH"
    postgres_db_auth_schema: str = "auth"
    postgres_user: str = "POSTGRES_USER"
    postgres_password: str = "POSTGRES_PASSWORD"

    redis_host: str = "127.0.0.1"
    redis_port: int = 6379
    redis_password: str = "REDIS_PASSWORD"
    dsl_auth: URL | None = None
    refresh_token_expires_in: int = 60
    access_token_expires_in: int = 30

    jwt_secret_key: str = "JWT_SECRET_KEY"
    jwt_algorithm: str = "JWT_ALGORITHM"

    admin_level: int = 5


settings = MyConfig()
settings.dsl_auth = URL.create(
    "postgresql+asyncpg",
    username=settings.postgres_user,
    password=settings.postgres_password,
    host=settings.postgres_host,
    port=settings.postgres_port,
    database=settings.postgres_db_auth,
)
