from http import HTTPStatus

from fastapi import Depends, HTTPException, APIRouter, Response
from fastapi_limiter.depends import RateLimiter

from services.auth_service import AuthorizationService, get_auth_service
from services.user_service import UserService, get_user_service
from services.password_service import pwd_context
from schemas import authorization, users
from tools.tokeniser import tokeniser
from tools.annotation import (
    LoginPassAnnotated,
    AccessTokenAnnotated,
    RefreshTokenAnnotated,
)


router = APIRouter()


@router.post(
    "/register",
    response_model=users.UserCreate,
    status_code=HTTPStatus.ACCEPTED,
    dependencies=[Depends(RateLimiter(times=1, seconds=5))],
)
async def register_user(
    common: LoginPassAnnotated = Depends(LoginPassAnnotated),
    user_service: UserService = Depends(get_user_service),
) -> users.User:

    check_user = await user_service.get_user(common.body.login)

    if check_user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail="login is already exists"
        )

    hashed_password = pwd_context.hash(common.body.password)

    user = await user_service.create_new_user(
        login=common.body.login,
        password=hashed_password,
    )

    return user


@router.post(
    "/authenticate",
    response_model=authorization.Auth,
    status_code=HTTPStatus.ACCEPTED,
    dependencies=[Depends(RateLimiter(times=1, seconds=5))],
)
async def authenticate_user(
    response: Response,
    common: LoginPassAnnotated = Depends(LoginPassAnnotated),
    auth_service: AuthorizationService = Depends(get_auth_service),
    user_service: UserService = Depends(get_user_service),
) -> authorization.Auth:

    user = await user_service.get_user(common.body.login)
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Incorrect login or password",
        )

    is_password_correct = pwd_context.verify(
        common.body.password, user.password
    )

    if not is_password_correct:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Incorrect login or password",
        )

    auth_data = await tokeniser(
        user,
        log_in=True,
        auth_service=auth_service,
        user_service=user_service,
    )

    response.set_cookie(key="access_token", value=auth_data["access_token"])
    response.set_cookie(key="refresh_token", value=auth_data["refresh_token"])

    return auth_data


@router.post(
    "/refresh",
    response_model=authorization.Auth,
    status_code=HTTPStatus.ACCEPTED,
    dependencies=[Depends(RateLimiter(times=1, seconds=5))],
)
async def refreshing_tokens(
    response: Response,
    common: RefreshTokenAnnotated = Depends(RefreshTokenAnnotated),
    auth_service: AuthorizationService = Depends(get_auth_service),
    user_service: UserService = Depends(get_user_service),
) -> authorization.Auth:

    login = await auth_service.check_refresh_token(common.body.refresh_token)

    if not login:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Incorrect refresh token",
        )

    user = await user_service.get_user(login)

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="Incorrect user"
        )

    auth_data = await tokeniser(
        user, auth_service=auth_service, user_service=user_service
    )

    response.set_cookie(key="access_token", value=auth_data["access_token"])
    response.set_cookie(key="refresh_token", value=auth_data["refresh_token"])

    return auth_data


@router.post(
    "/logout",
    response_model=users.UserBase,
    status_code=HTTPStatus.ACCEPTED,
    dependencies=[Depends(RateLimiter(times=1, seconds=5))],
)
async def logout(
    common: AccessTokenAnnotated = Depends(AccessTokenAnnotated),
    auth_service: AuthorizationService = Depends(get_auth_service),
):

    login, role = await auth_service.check_access_token(
        common.body.access_token
    )

    if not login:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Incorrect access token",
        )

    await auth_service.logout(login, common.body.access_token)

    return {"login": login}


@router.post(
    "/check",
    response_model=users.UserBase,
    status_code=HTTPStatus.ACCEPTED,
    # dependencies=[Depends(RateLimiter(times=1, seconds=5))],
)
async def check(
    common: AccessTokenAnnotated = Depends(AccessTokenAnnotated),
    auth_service: AuthorizationService = Depends(get_auth_service),
):
    login, role = await auth_service.check_access_token(common.body.access_token)

    if not login:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Incorrect access token",
        )

    # await auth_service.logout(login, common.body.access_token)

    return {"login": login}
