import uuid

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas import ProductPostQuery
from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Product, Subject, Image
from commons.neuro_gateway.mistral import Mistral
from commons.neuro_gateway.stable_diffusion import StableDiffusion
from commons.utils import download_product_image
from commons.core.image_core import ImageCore


image_core = ImageCore()
settings = get_settings()
sd = StableDiffusion(settings.mistral_api_key)

router = APIRouter()

@router.get('/')
async def get_products_by_subject_id(
    subject_id: int | None = None,
    db: AsyncSession = Depends(get_async_db)):

    stmt = select(Product)

    if subject_id:
        print(subject_id)
        stmt = stmt.where(Product.subject_id == subject_id)

    result = await db.scalars(stmt)
    return {"status": True, "result": [*result]}


@router.post('/')
async def create_product(
    request: ProductPostQuery,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_async_db)
    ):

    subject_id = request.subject_id
    product_name = request.product_name

    subject = await db.scalar(select(Subject).where(Subject.id == subject_id))

    if not subject:
        return {
            'status': False, 
            'error': 'Указанной категории не существует',
            }
    
    result = await db.scalar(select(Product).where(Product.name == product_name))
    
    if result:
        return {
            'status': False, 
            'message': 'Данный продукт уже существует'
            }
    
    product = Product(name=product_name, subject=subject)

    img_uuid = uuid.uuid4()
    image = Image(uuid=img_uuid, product=product)
    
    db.add_all([product, image])
    
    await db.commit()

    product = await db.scalar(select(Product).where(Product.name == product_name))

    background_tasks.add_task(download_product_image,
                              image_core,
                              db,
                              product_name,
                            #   settings.staticfiles_path,
                              img_uuid)

    
    return {'status': True, 
            'result': product,
            }


@router.post('/auto')
async def create_product_auto(
    request: ProductPostQuery, db: AsyncSession = Depends(get_async_db)
    ):  
    
    # products_list = await db.scalars(select(Product.name))

    # except_words = ",".join([*products_list])

    # subject_name = request.subject_name
    # product_name = get_product(mistral, subject_name, except_words)
    # product_name = product_name.strip('"')

    # subject = await db.scalar(select(Subject).where(Subject.name == subject_name))

    # db.add(Product(
    #     name = product_name,
    #     description = '',
    #     subject=subject,))
    
    # await db.commit()

    return {'status': True, 'message': f'Продукт {""} создан'}