from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Subject

settings = get_settings()

router = APIRouter()

@router.get('/')
async def get_all_subject(db: AsyncSession = Depends(get_async_db)):
    stmt = select(Subject)
    result = await db.scalars(stmt)
    return {"status": True, "result": [*result]}
