import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from commons.config import get_settings
from commons.db import get_async_db
from commons.models import Post, Product, Image
from app.core.schemas import PostsPostQuery

settings = get_settings()

router = APIRouter()

@router.get('/')
async def get_all_posts(db: AsyncSession = Depends(get_async_db)):
    result = await db.scalars(select(Post))
    return {
        'status': True, 
        'result': result
        }


@router.post('/')
async def create_post(
    request: PostsPostQuery,
    db: AsyncSession = Depends(get_async_db)):

    product_id = request.product_id
    prompt = request.prompt

    product = await db.scalar(select(Product).where(Product.id == product_id))

    post = Post(product=product, query=prompt)

    img_uuid = uuid.uuid4()
    image = Image(uuid=img_uuid, post=post)

    db.add_all([post, image])
    await db.flush()
    await db.refresh(post)

    post_id = post.id

    await db.commit()

    result = await db.scalar(select(Post).where(Post.id == post_id))

    return {
        'status': True,
        'result': result,
    }
