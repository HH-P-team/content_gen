import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from db.base_storage import BaseUserStore
from db.pg_executor import PgExecutor
from db.models.users import Users


class PgUserStoreTools(PgExecutor, BaseUserStore):

    @PgExecutor.async_session_executor
    async def create_user(
        self,
        name: str,
        surname: str,
        mail: str,
        login: str,
        password: str,
        session: Session,
    ) -> Users:

        user = Users(
            name=name,
            surname=surname,
            email=mail,
            login=login,
            password=password,
        )

        session.add(user)
        return user

    @PgExecutor.async_session_executor
    async def get_user(self, login: str, session: Session = None) -> Users:

        query_user = select(Users).where(Users.login == login)
        query_user_result = await session.execute(query_user)
        user = query_user_result.scalar_one()
        return user

    @PgExecutor.async_session_executor
    async def get_user_by_uuid(
        self, uuid: uuid.UUID, session: Session = None
    ) -> Users:

        query_user = select(Users).where(Users.uuid == uuid)
        query_user_result = await session.execute(query_user)
        user = query_user_result.scalar_one()
        return user

    @PgExecutor.async_session_executor
    async def update_user(
        self, user_uuid: uuid.UUID, session: Session, **kwargs
    ):

        user = await self.get_user_by_uuid(user_uuid)

        if user:
            for attr, value in kwargs.items():
                user.__setattr__(attr, value)
            session.add(user)
        return user
