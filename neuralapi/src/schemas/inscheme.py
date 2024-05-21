from typing import Literal

from pydantic import BaseModel


class UserReq(BaseModel):
    text: str
    category: Literal[
        "beauty", "education", "relax", "restuarants", "dress", "free"
    ] = "free"
