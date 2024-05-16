from typing import AsyncGenerator, Generator

from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import Session

from commons.config import get_settings

settings = get_settings()

engine: Engine = create_engine(settings.database_uri.unicode_string(), echo=True)
async_engine: AsyncEngine = create_async_engine(
    settings.async_database_uri.unicode_string(),
    echo=True,
    )

def get_db() -> Generator[Session, None, None]:
    """
    """

    with Session(engine) as session:
        yield session

async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """
    """
    async with AsyncSession(async_engine) as session:
        yield session
