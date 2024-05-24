from uuid import UUID
from typing import Literal

from pydantic import BaseModel


class UserReq(BaseModel):
    text: str
    file: bool = False
    uuid: UUID
    category: Literal[
        "beauty", "education", "relax", "restuarants", "dress", "free"
    ] = "free"
