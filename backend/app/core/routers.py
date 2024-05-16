from sqlalchemy import select
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from commons.db import get_async_db
from commons.models import Subject, Product, Post

router = APIRouter(
    prefix="/api/v1",
    tags=["api"],
    default_response_class=JSONResponse,
)


@router.get('/subjects')
async def get_subject(db=Depends(get_async_db)):
    stmt = select(Subject)
    result = await db.scalars(stmt)
    return {'status': True, 'result': [*result]}


@router.get('/products')
async def get_subject(db=Depends(get_async_db)):
    stmt = select(Product)
    result = await db.scalars(stmt)
    return {'status': True, 'result': [*result]}


@router.get('/posts')
async def get_subject(db=Depends(get_async_db)):
    stmt = select(Post)
    result = await db.scalars(stmt)
    return {'status': True, 'result': [*result]}