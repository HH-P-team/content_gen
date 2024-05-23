from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Subject
from app.core.schemas import SubjectPostQuery, SubjectResponseList, SubjectModel

settings = get_settings()

router = APIRouter()

@router.get('/')
async def get_all_subject(id: int = 0, db: AsyncSession = Depends(get_async_db)):
    stmt = select(Subject.id, Subject.name)
    result = await db.execute(stmt)
    return {"status": True, "result": result.mappings().all()}


@router.post('/')
async def create_subject(
    request: SubjectPostQuery, db: AsyncSession = Depends(get_async_db)
):  
    #TODO убрать проверки, добавить ограничение на уникальность имени
    name = request.subject_name
    stmt = select(Subject).where(Subject.name == name)
    result = await db.scalar(stmt)

    if result:
        return {'status': False, 'message': 'Данная категория уже существует'}
    
    db.add(Subject(name=name))
    await db.commit()

    stmt = select(Subject).where(Subject.name == name)
    result = await db.scalar(stmt)

    return {'status': True, 
            'result': {'name': result.name,
                       'id': result.id,
                       }}
