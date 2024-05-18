from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas import ImagePostQuery
from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Image, Subject
from commons.neuro_gateway.stable_diffusion import StableDiffusion


settings = get_settings()
sd = StableDiffusion(settings.mistral_api_key)

router = APIRouter()


@router.post("/")
async def get_image(
    image: ImagePostQuery, db: AsyncSession = Depends(get_async_db)
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
