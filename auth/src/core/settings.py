import logging
from logging import config as logging_config

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

from core.logger import LOGGING


logging_config.dictConfig(LOGGING)
logger = logging.getLogger("AuthService")


class MyConfig(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    project_name: str = "auth"

    auth_host: str = "localhost"
    auth_port: int = 8000

    pg_host: str = "127.0.0.45"
    pg_port: int = 5432

    auth_postgres_host: str = "localhost"
    auth_postgres_port: str = 5433

    auth_postgres_db_name: str = "POSTGRES_DB_AUTH"
    auth_postgres_scheme: str = "auth"

    auth_postgres_user: str = "AUTH_POSTGRES_USER"
    auth_postgres_password: str = "AUTH_POSTGRES_PASSWORD"

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
    username=settings.auth_postgres_user,
    password=settings.auth_postgres_password,
    host=settings.auth_postgres_host,
    port=settings.auth_postgres_port,
    database=settings.auth_postgres_db_name,
)
