from pydantic import BaseModel

class ImagePostQuery(BaseModel):
    message: str