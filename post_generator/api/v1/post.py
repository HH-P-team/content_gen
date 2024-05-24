from fastapi import APIRouter, Depends


from schemas.post import InputPrompt, Post
from services.post import PostService, get_post_service

from core.logger import logger

router = APIRouter()


@router.post(
    "/",
    response_model=Post,
)
async def generate(
    prompt: InputPrompt,
    post_service: PostService = Depends(get_post_service),
) -> Post:
    logger.info(f"Input prompt: {prompt}")
    data = post_service.generate_post(input_prompt=prompt)
    logger.info(f"Response data: {data}")

    return data
