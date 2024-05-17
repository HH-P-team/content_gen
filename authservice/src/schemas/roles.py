import uuid

from schemas.basejason import BaseOrjsonModel


class RoleBase(BaseOrjsonModel):
    name: str
    desc: str | None = None
    level: int


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    pass
    uuid: uuid.UUID
