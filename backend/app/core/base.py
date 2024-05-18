from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.core.routers.subjects import router as subject_router
from app.core.routers.images import router as image_router
from app.core.routers.products import router as product_router
from app.core.routers.posts import router as post_router
from commons.config import get_settings
from commons.utils import get_products


settings = get_settings()

router = APIRouter(
    prefix=settings.api_prefix,
    tags=["api"],
    default_response_class=JSONResponse,
)

router.include_router(
    subject_router,
    prefix='/subjects',
    )

router.include_router(
    image_router,
    prefix='/image',
    )

router.include_router(
    product_router,
    prefix='/products',
    )

router.include_router(
    post_router,
    prefix='/posts',
    )
