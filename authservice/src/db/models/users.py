import uuid
import asyncio
from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey

from sqlalchemy.orm import declarative_base, declarative_mixin, relationship
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.dialects.postgresql import UUID

from core.settings import settings


Base = declarative_base()


@declarative_mixin
class BaseModelMixin:

    __table_args__ = {"schema": settings.postgres_db_auth_schema}

    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )
    create_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    update_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


class Users(Base, BaseModelMixin):
    __tablename__ = "users"

    name = Column(String(128))
    surname = Column(String(128))
    login = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), unique=True)
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return (
            f"uuid: {self.uuid} name: {self.name}"
            f" surname: {self.surname} login: {self.login}"
            f" e-mail: {self.email}"
        )

    def to_dict(self) -> dict[str, str]:
        return {
            "uuid": self.uuid,
            "email": self.email,
            "login": self.login,
        }


class Account(Base):
    __tablename__ = "account"
    __table_args__ = {"schema": settings.postgres_db_auth_schema}

    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )
    user_uuid = Column(
        UUID(as_uuid=True),
        ForeignKey(
            f'{__table_args__["schema"]}.users.uuid', ondelete="CASCADE"
        ),
    )

    login_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    user = relationship("Users")

    def __repr__(self):
        return (
            f"uuid: {self.uuid} user_uuid: {self.user_uuid} "
            f"login_time: {self.login_time}"
        )

    def to_dict(self) -> dict[str, str]:
        return {
            "uuid": self.uuid,
            "user_uuid": self.user_uuid,
            "e-mail": self.email,
            "login_time": self.login_time,
        }


async def create_scheme():

    engine = create_async_engine(settings.dsl_auth)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_scheme())
