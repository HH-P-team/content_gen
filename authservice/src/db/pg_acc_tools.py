import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session, Load

from db.pg_executor import PgExecutor
from db.base_storage import BaseAccStore
from db.models.users import Account


class PgAccStoreTools(PgExecutor, BaseAccStore):

    @PgExecutor.async_session_executor
    async def add_acc(
        self,
        user_uuid: uuid.UUID,
        session: Session
    ) -> Account:

        acc = Account(user_uuid=user_uuid)

        session.add(acc)
        return acc

    @PgExecutor.async_session_executor
    async def get_acc_table(
        self,
        user_uuid: uuid.UUID,
        session: Session
    ) -> Account:

        query_acc_table = select(Account).options(
            Load(Account)).where(Account.user_uuid == user_uuid)
        query_acc_table_result = await session.execute(query_acc_table)
        acc_table = query_acc_table_result.scalars().all()

        return acc_table
