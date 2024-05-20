from http import HTTPStatus

from fastapi import Depends, HTTPException, APIRouter, Response

imaging_router = APIRouter()


@imaging_router.get(
    "/image",
    # response_model=users.UserCreate,
    status_code=HTTPStatus.ACCEPTED,
    # dependencies=[Depends(RateLimiter(times=1, seconds=5))],
)
async def register_user(
    # common: LoginPassAnnotated = Depends(LoginPassAnnotated),
    # user_service: UserService = Depends(get_user_service),
) -> dict:
    return {"resp" " OK"}
