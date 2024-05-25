from sqlalchemy import bindparam, update
from sqlalchemy.ext.asyncio import AsyncSession

from commons.models import Image
from commons.neuro_gateway.mistral import Mistral
from commons.neuro_gateway.stable_diffusion import StableDiffusion
from commons.core.image_core import ImageCore

def get_product(api: Mistral, subject: str) -> str:
    """
    """
    return api.send_message(
        f'Действуй в качестве маркетолога, выполни задачу придумай название коммерческого продукта, подходящего под категорию {subject}. В виде названия не более 3 слов'
        )

def get_products(api: Mistral, subject: str) -> str:
    """
    """
    return api.send_message(
        f'Придумай названия 5 коммерческих продуктов подходящих под категорию {subject}'
        )

def get_post_description(api: Mistral, subject: str) -> str:
    """
    """
    return api.send_message(
        f'Напиши пост рекламного характера на следующую тематику: {subject}'
        )

# async def download_subject_image(
#         api: StableDiffusion,
#         db: AsyncSession,
#         name: str, 
#         filepatch: str,
#         filename: str) -> None:
#     """
#     """

#     api.get_image(name, filepatch, filename)
#     await db.execute(update(Image)
#                .where(Image.uuid == filename)
#                .values(in_progress=False))
    
#     await db.commit()


async def download_subject_image(
        api: ImageCore,
        db: AsyncSession,
        text: str, 
        filename: str) -> None:
    """
    """

    api.create_image(filename, text)
    await db.execute(update(Image)
               .where(Image.uuid == filename)
               .values(in_progress=False))
    
    await db.commit()


# async def download_product_image(
#         api: StableDiffusion,
#         db: AsyncSession,
#         name: str, 
#         filepatch: str,
#         filename: str) -> None:
#     """
#     """

#     api.get_image(name, filepatch, filename)
#     await db.execute(update(Image)
#                .where(Image.uuid == filename)
#                .values(in_progress=False))
    
#     await db.commit()

async def download_product_image(
        api: ImageCore,
        db: AsyncSession,
        text: str, 
        # filepatch: str,
        filename: str) -> None:
    """
    """

    api.create_image(filename, text)
    await db.execute(update(Image)
               .where(Image.uuid == filename)
               .values(in_progress=False))
    
    await db.commit()


subjects_img = {'Образование': 'education',
            'Бьюти индустрия': 'beauty',
            'Одежда': 'dress',
            'Отдых': 'relax',
            'Рестораны и Кафе': 'restuarants',
            }

async def download_post_image(
        api: ImageCore,
        db: AsyncSession,
        text: str,
        product_name: str,
        filename: str) -> None:
    """
    """

    category = subjects_img.get('product_name', 'free')

    api.create_image(filename, text, category)
    
    await db.execute(update(Image)
            .where(Image.uuid == filename)
            .values(in_progress=False))
    
    await db.commit()
    