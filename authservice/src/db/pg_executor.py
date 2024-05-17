from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from core.settings import settings, logger


class PgExecutor():

    def __init__(self) -> None:
        self.engine = create_async_engine(settings.dsl_auth)

    def async_session_executor(proc):
        async def wrapper(*args, **kwargs):
            self = args[0]
            engine = self.engine
            async_sesion_factory = sessionmaker(
                engine,
                expire_on_commit=False,
                class_=AsyncSession
            )
            async with async_sesion_factory() as session:
                async with session.begin():
                    try:
                        res = await proc(*args, **kwargs, session=session)
                    except NoResultFound as e:
                        logger.error(
                            f'error: {e}  function: {proc.__name__} args {args} kwargs {kwargs}'
                        )
                        return None
            return res
        return wrapper
