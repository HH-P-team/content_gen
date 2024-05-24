import uuid

from fastapi import APIRouter,BackgroundTasks, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas import SubjectPostQuery, SubjectResponseList, SubjectModel
from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Image, Subject
from commons.neuro_gateway.stable_diffusion import StableDiffusion
from commons.utils import download_subject_image


settings = get_settings()
sd = StableDiffusion(settings.mistral_api_key)

router = APIRouter()

@router.get('/')
async def get_all_subject(id: int = 0, db: AsyncSession = Depends(get_async_db)):
    result = await db.scalars(select(Subject))
    return {
        'status': True,
        'result': result.fetchall()
        }


@router.post('/')
async def create_subject(
    request: SubjectPostQuery,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_async_db),
):  
    #TODO убрать проверки, добавить ограничение на уникальность имени
    name = request.subject_name
    stmt = select(Subject).where(Subject.name == name)
    result = await db.scalar(stmt)

    if result:
        return {
            'status': False, 
            'message':'Данная категория уже существует'
            }
    
    img_uuid = str(uuid.uuid4())

    subject = Subject(name=name)
    image = Image(uuid=img_uuid, subject=subject)
    db.add_all([subject, image])

    await db.commit()

    subject = await db.scalar(select(Subject).where(Subject.name == name))

    background_tasks.add_task(download_subject_image,
                              sd,
                              db,
                              name,
                              settings.staticfiles_path,
                              img_uuid)

    return {
        'status': True, 
        'result': result
        }
