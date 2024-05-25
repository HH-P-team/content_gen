import uuid

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Post, Product, Image
from app.core.schemas import PostsPostQuery
from commons.core.image_core import ImageCore
from commons.core.text_core import TextCore
from commons.utils import download_post_image

settings = get_settings()
image_core = ImageCore()
text_core = TextCore()

router = APIRouter()

subjects_txt = {'Образование': 'education',
            'Бьюти индустрия': 'beauty',
            'Одежда': 'clothes',
            'Отдых': 'vacation',
            'Рестораны и Кафе': 'restuarants',
            }

@router.get('/')
async def get_all_posts(db: AsyncSession = Depends(get_async_db)):
    result = await db.scalars(select(Post))
    return {
        'status': True, 
        'result': result.fetchall()
        }


@router.post('/')
async def create_post(
    request: PostsPostQuery,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_async_db)):

    product_id = request.product_id
    prompt = request.prompt

    product = await db.scalar(select(Product).where(Product.id == product_id))

    product_name = product.name

    post = Post(product=product, query=prompt)

    img_uuid = uuid.uuid4()
    image = Image(uuid=img_uuid, post=post)

    db.add_all([post, image])
    await db.flush()
    await db.refresh(post)

    post_id = post.id

    await db.commit()

    background_tasks.add_task(download_post_image,
                              image_core,
                              db,
                              prompt,
                              product_name,
                              img_uuid)
    
    category = subjects_txt.get(product_name, 'clothes')
    
    text = text_core.create_text(category, product_name)['result']

    await db.execute(update(Post).where(Post.id == post_id).values(description=text))
    await db.commit()
    
    result = await db.scalar(select(Post).where(Post.id == post_id))

    return {
        'status': True,
        'result': result,
    }
