from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas import ImageQuery, ImageSubjectQuery, ImageProductQuery, ImagePostQuery
from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Image, Subject, Product, Post
from commons.neuro_gateway.stable_diffusion import StableDiffusion


settings = get_settings()
sd = StableDiffusion(settings.mistral_api_key)

router = APIRouter()


@router.post('/')
async def get_image(
    image: ImageQuery, db: AsyncSession = Depends(get_async_db)
):
    name = image.message
    img_payload = b''
    subject = await db.scalar(select(Subject).where(Subject.name == name))

    if not subject:
        return {"status": False}

    if subject.image:
        img_payload = subject.image.payload

    if not img_payload:
        img_payload = sd.get_image_payload_b64(name)
        db.add(Image(payload=img_payload, subject=subject))
        await db.commit()

    return {"status": True, "result": img_payload}


@router.post('/subject')
async def get_image_by_subject_id(
    request: ImageSubjectQuery, db: AsyncSession = Depends(get_async_db)
):
    print(request)
    subject_id = request.subject_id
    subject = await db.scalar(select(Subject).where(Subject.id == subject_id))
    
    if not subject:
        return {"status": False}
    
    if subject.image:
        return {"status": True, "result": subject.image.payload}
    

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
