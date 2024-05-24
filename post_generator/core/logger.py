import os
import sys
import logging

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DEFAULT_HANDLERS = [
    "console",
]

# Настраивается логирование uvicorn-сервера
# Про логирование в Python можно прочитать в документации
# https://docs.python.org/3/howto/logging.html
# https://docs.python.org/3/howto/logging-cookbook.html

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": LOG_FORMAT},
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": "%(levelprefix)s %(client_addr)s - '%(request_line)s' %(status_code)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {
            "handlers": LOG_DEFAULT_HANDLERS,
            "level": "INFO",
        },
        "uvicorn.error": {
            "level": "INFO",
        },
        "uvicorn.access": {
            "handlers": ["access"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "level": "INFO",
        "formatter": "verbose",
        "handlers": LOG_DEFAULT_HANDLERS,
    },
}


class Logger:
    """
    A simple logger class that can be used to log messages to the console.

    Attributes:
        instance (Logger): A single instance of the Logger class.
    """

    def __new__(cls):
        """
        Creates a new instance of the Logger class if it does not already exist.

        Returns:
            Logger: The single instance of the Logger class.
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(Logger, cls).__new__(cls)
            cls.set_base_config()

        return cls.instance

    @classmethod
    def set_base_config(cls):
        """
        Sets the base logging configuration for the Logger class.

        This includes setting the log level and configuring the console handler.
        """
        log_level = str(os.getenv("LOG_LEVEL", "INFO")).upper()
        level = logging.getLevelName(log_level)

        log_format = "%(asctime)s : %(name)s : %(levelname)s : %(module)s : %(message)s"
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(log_format))

        logging.basicConfig(level=level, handlers=[console_handler])

    def get_logger(self, name: str = "core", debug: bool = False) -> logging.Logger:
        """
        Returns a python logger with the given name and debug level.

        Args:
            name (str, optional): The name of the logger. Defaults to "core".
            debug (bool, optional): Whether to set the debug level of the logger. Defaults to False.

        Returns:
            logging.Logger: The python logger with the given name and debug level.
        """
        logger = logging.getLogger(name)
        if debug:
            logger.setLevel(logging.DEBUG)

        return logger


logger = Logger().get_logger(debug=True)
