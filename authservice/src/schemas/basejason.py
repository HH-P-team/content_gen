import orjson
from tools.jsontools import orjson_dumps

from pydantic import BaseModel


class BaseOrjsonModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
