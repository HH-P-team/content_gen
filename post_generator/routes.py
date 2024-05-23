from fastapi import APIRouter, Depends

from api.v1 import post


routes = APIRouter()


routes.include_router(
    post.router,
    prefix="/api/v1/post",
    tags=["post"],
    dependencies=[],
)
