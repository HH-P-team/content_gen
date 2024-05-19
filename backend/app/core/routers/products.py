from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas import ProductPostQuery
from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Product, Subject
from commons.neuro_gateway.mistral import Mistral
from commons.utils import get_product


settings = get_settings()
mistral = Mistral(settings.mistral_api_key)

router = APIRouter()

@router.get('/')
async def get_all_product(db: AsyncSession = Depends(get_async_db)):
    stmt = select(Product)
    result = await db.scalars(stmt)
    return {"status": True, "result": [*result]}


# @router.post('/')
# async def create_product(
#     request: ProductPostQuery, db: AsyncSession = Depends(get_async_db)
# ):  
#     #TODO убрать проверки, добавить ограничение на уникальность имени
#     name = request.name
#     stmt = select(Product).where(Product.name == name)
#     result = await db.scalar(stmt)

#     if result:
#         return {'status': False, 'message': 'Даннуже существует'}
    

#     db.add(Subject(name=name))
#     await db.commit()
#     return {'status': True, 'message': 'Категория успешно добавлена'}

@router.post('/auto')
async def create_product_auto(
    request: ProductPostQuery, db: AsyncSession = Depends(get_async_db)
):  
    
    products_list = await db.scalars(select(Product.name))

    except_words = ",".join([*products_list])

    subject_name = request.subject_name
    product_name = get_product(mistral, subject_name, except_words)
    product_name = product_name.strip('"')

    subject = await db.scalar(select(Subject).where(Subject.name == subject_name))

    db.add(Product(
        name = product_name,
        description = '',
        subject=subject,))
    
    await db.commit()

    return {'status': True, 'message': f'Продукт {""} создан'}