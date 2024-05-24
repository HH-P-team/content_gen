import uuid

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas import ImageQuery, ImageSubjectQuery, ImageProductQuery, ImagePostQuery
from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Image, Subject, Product, Post
from commons.neuro_gateway.stable_diffusion import StableDiffusion
from commons.utils import download_subject_image


settings = get_settings()
sd = StableDiffusion(settings.mistral_api_key)

router = APIRouter()


@router.post('/')
async def get_image(
    request: ImageQuery,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_async_db),
):
    name = request.message
    subject = await db.scalar(select(Subject).where(Subject.name == name))

    if not subject:
        return {
            'status': False, 
            'error': 'Категория с данным именем отсутствует',
            }

    if subject.image:
        return {
            'status': True,
            'result': subject.image,
        }

    else:
        img_uuid = str(uuid.uuid4())
        db.add(Image(uuid=img_uuid, subject=subject))
        await db.commit()
        image = await db.scalar(select(Image).where(Image.uuid == img_uuid))

        background_tasks.add_task(
            download_image, sd, db, name, settings.staticfiles_path, img_uuid)

    return {'status': True, 'result': image}


@router.post('/subject')
async def get_image_by_subject_id(
    request: ImageSubjectQuery, db: AsyncSession = Depends(get_async_db)
):
    subject_id = request.subject_id
    subject = await db.scalar(select(Subject).where(Subject.id == subject_id))
    
    if not subject:
        return {
            "status": False,
            'error': 'Категория с данным ID отсутствует'
            }
    
    if subject.image:
        return {
            'status': True,
            'result': subject.image,
            }
    

@router.post('/product')
async def get_image_by_product_id(
    request: ImageProductQuery, db: AsyncSession = Depends(get_async_db)
):
    product_id = request.product_id
    product = await db.scalar(select(Product).where(Product.id == product_id))
    
    if not product:
        return {"status": False}
    
    image = await db.scalar(select(Image).where(Image.product_id == product_id))

    if not image:
        img_payload = sd.get_image_payload_b64(product.name)
        db.add(Image(payload=img_payload, product=product))
        await db.commit()

    else:
        img_payload = image.payload
    
    return {"status": True, "result": img_payload}
