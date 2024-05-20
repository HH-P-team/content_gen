from typing import Optional

from pydantic import BaseModel

class ImagePostQuery(BaseModel):
    message: str


class SubjectPostQuery(BaseModel):
    name: str

class SubjectModel(BaseModel):
    id: int
    name: str

class SubjectResponseList(BaseModel):
    subjects: list = list[SubjectModel]

    

class ProductPostQuery(BaseModel):
    name: Optional[str] = None
    subject_name: str
    subject_id: Optional[int] = None
