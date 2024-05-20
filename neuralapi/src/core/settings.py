import logging
from logging import config as logging_config

from pydantic_settings import BaseSettings, SettingsConfigDict

from core.logger import LOGGING


logging_config.dictConfig(LOGGING)
logger = logging.getLogger("neuralapi-service")


class MyConfig(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    project_name: str = "neuralapi"

    auth_host: str = "localhost"
    auth_port: int = 8012


settings = MyConfig()
