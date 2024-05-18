from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas import ImagePostQuery
from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Image, Subject, Product, Post
from commons.neuro_gateway.stable_diffusion import StableDiffusion
from commons.utils import get_products

settings = get_settings()
sd = StableDiffusion(settings.mistral_api_key)

router = APIRouter(
    prefix=settings.api_prefix,
    tags=["api"],
    default_response_class=JSONResponse,
)


@router.get('/subjects')
async def get_subject(db=Depends(get_async_db)):
    stmt = select(Subject)
    result = await db.scalars(stmt)
    return {'status': True, 'result': [*result]}


@router.get('/products')
async def get_subject(db: AsyncSession = Depends(get_async_db)):
    stmt = select(Product)
    result = await db.scalars(stmt)
    return {'status': True, 'result': [*result]}


@router.get('/posts')
async def get_subject(db=Depends(get_async_db)):
    stmt = select(Post)
    result = await db.scalars(stmt)
    return {'status': True, 'result': [*result]}


@router.post('/image')
async def get_image(image: ImagePostQuery, db: AsyncSession = Depends(get_async_db)):
    name = image.message
    img_payload = b''
    subject = await db.scalar(select(Subject).where(Subject.name == name))
    
    if not subject:
        return {'status': False}
    
    if subject.image:
        img_payload = subject.image.payload
    
    if not img_payload:
        img_payload = sd.get_image_payload_b64(name)
        db.add(Image(payload=img_payload, subject=subject))
        await db.commit()

    return {'status': True, 'result': img_payload}