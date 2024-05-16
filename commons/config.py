from functools import lru_cache
from typing import Any, Optional, Union

from pydantic import Field, field_validator, PostgresDsn
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Настройки окружения
    """

    mistral_api_key: str = Field(alias='MISTRAL_API_KEY')

    pg_host: str = Field(alias='POSTGRES_HOST')
    pg_user: str = Field(alias='POSTGRES_USER')
    pg_password: str = Field(alias='POSTGRES_PASSWORD')
    pg_database: str = Field(alias='POSTGRES_DB_NAME')
    pg_port: int = Field(alias='POSTGRES_PORT')

    database_uri: Union[PostgresDsn, str] = Field(default='')
    async_database_uri: Union[PostgresDsn, str] = Field(default='')

    api_port: int = Field(alias='API_PORT')

    @field_validator('database_uri')
    def assemble_db_connection(
        cls, 
        value: Optional[str],
        info: FieldValidationInfo,
    ) -> Any:
        """Схема подключения к БД"""
        if isinstance(value, str) and value == '':
            return PostgresDsn.build(
                scheme='postgresql+psycopg2',
                username=info.data['pg_user'],
                password=info.data['pg_password'],
                host=info.data['pg_host'],
                port=info.data['pg_port'],
                path=info.data['pg_database'],
            )
        return value
    
    @field_validator('async_database_uri')
    def assemble_db_async_connection(
            cls, value: Optional[str], info: FieldValidationInfo,
    ) -> Any:
        """Схема асинхронного подключения к БД"""
        if isinstance(value, str) and value == '':
            return PostgresDsn.build(
                scheme='postgresql+asyncpg',
                username=info.data['pg_user'],
                password=info.data['pg_password'],
                host=info.data['pg_host'],
                port=info.data['pg_port'],
                path=info.data['pg_database'],
            )
        return value
    

@lru_cache
def get_settings() -> Settings:
    """
    Возвращает настройки окружения. Запрос происходит один
    раз, во время запуска проекта
    """
    return Settings()
