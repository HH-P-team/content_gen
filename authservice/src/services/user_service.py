import uuid

from fastapi import Depends

from db.base_storage import BaseUserStore
from db.pg_user_tools import PgUserStoreTools
from db.models.users import Users


class UserService:

    def __init__(self, user_db: BaseUserStore, acc_db: BaseAccStore):
        self.user_db = user_db
        self.acc_db = acc_db

    async def create_new_user(
        self,
        login: str,
        password: str,
        name: str = None,
        surname: str = None,
        mail: str = None,
    ):

        user = await self.user_db.create_user(
            name,
            surname,
            mail,
            login,
            password,
        )

        return user

    async def get_user(self, login: str) -> Users:
        user = await self.user_db.get_user(login)
        return user

    async def get_user_by_uuid(self, uuid: uuid.UUID) -> Users:
        user = await self.user_db.get_user_by_uuid(uuid)
        return user

    async def update_user(self, user_uuid: uuid.UUID, **kwargs) -> Users:

        user = await self.user_db.update_user(user_uuid, **kwargs)
        return user

    async def acc_login(self, user_uuid: uuid.UUID):
        acc = await self.acc_db.add_acc(user_uuid)
        if acc:
            return acc.login_time

    async def get_acc_info(self, user_uuid: uuid.UUID):
        acc_info = await self.acc_db.get_acc_table(user_uuid)
        return acc_info


def get_user_service(
    user_db: BaseUserStore = Depends(PgUserStoreTools),
) -> UserService:

    return UserService(user_db)
