from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas import ProductPostQuery
from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Product, Subject
from commons.neuro_gateway.mistral import Mistral
from commons.utils import get_product

from typing import Optional


settings = get_settings()
mistral = Mistral(settings.mistral_api_key)

router = APIRouter()

@router.get('/')
async def get_products_by_subject_id(subject_id: int | None = None, db: AsyncSession = Depends(get_async_db)):
    stmt = select(Product)

    if subject_id:
        print(subject_id)
        stmt = stmt.where(Product.subject_id == subject_id)

    result = await db.scalars(stmt)
    return {"status": True, "result": [*result]}


@router.post('/')
async def create_product(
    request: ProductPostQuery, db: AsyncSession = Depends(get_async_db)
    ):
    subject_id = request.subject_id
    subject = await db.scalar(select(Subject).where(Subject.id == subject_id))
    product_name = get_product(mistral, subject.name)

    db.add(Product(
        name=product_name,
        subject=subject,
        description='',))
    
    await db.commit()

    product = await db.scalar(select(Product).where(Product.name == product_name))
    
    return {'status': True, 
            'result': {
                'name': product.name,
                'id': product.id,
            }}


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