from enum import Enum

from pydantic import BaseModel


class CategoryEnum(Enum):
    clothes = "clothes"
    beauty = "beauty"
    education = "education"
    restaurant = "restaurant"
    vacation = "vacation"
    base = "base"


class InputPrompt(BaseModel):
    category: CategoryEnum
    prompt: str = ""


class Post(BaseModel):
    category: CategoryEnum
    input_prompt: str
    result: str
