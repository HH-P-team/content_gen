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

    ext_api_timeout: int = 1000

    dataset_beauty_path: str = "datasets/beauty"
    dataset_education_path: str = "datasets/education"
    dataset_relax_path: str = "datasets/relax"
    dataset_restuarants_path: str = "datasets/restuarants"
    dataset_dress_path: str = "datasets/dress"

    path_to_downloads: str = "downloads"
    path_to_arts: str = "arts"

    sd_keys: str | list = "a, b, c"
    fb_api_key: str = "api_key"
    fb_secret_key: str = "secret_key"

    giga_key: str = "giga_key"


settings = MyConfig()
settings.sd_keys.split(",")
