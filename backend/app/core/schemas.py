from typing import Optional

from pydantic import BaseModel

class ImageQuery(BaseModel):
    message: str

class ImageSubjectQuery(BaseModel):
    subject_id: int

class ImageProductQuery(BaseModel):
    product_id: int

class ImagePostQuery(BaseModel):
    post_id: int

class SubjectPostQuery(BaseModel):
    subject_name: str

class SubjectModel(BaseModel):
    id: int
    name: str

class SubjectResponseList(BaseModel):
    subjects: list = list[SubjectModel]

class ProductPostQuery(BaseModel):
    subject_id: int
    product_name: str

class PostsPostQuery(BaseModel):
    product_id: int
    prompt: str

