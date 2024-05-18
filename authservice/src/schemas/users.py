from uuid import UUID

from schemas.basejason import BaseOrjsonModel


class UserBase(BaseOrjsonModel):
    login: str


class UserCreate(UserBase):
    uuid: UUID


class User(UserCreate):
    name: str | None = None
    surname: str | None = None
    phone: str | None = None
    email: str | None = None
