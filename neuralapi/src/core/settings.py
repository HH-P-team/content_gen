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

    app_name: str = "neuralapi"
    app_host: str = "localhost"
    app_port: int = 8012

    ext_api_timeout: int = 100


settings = MyConfig()
