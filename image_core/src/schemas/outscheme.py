from uuid import UUID

from pydantic import BaseModel


class ImageResp(BaseModel):
    promt: str
    time: float
    classification: dict
    path: str
    uuid: UUID
