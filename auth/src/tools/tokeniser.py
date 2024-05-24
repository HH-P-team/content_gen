from db.models.users import Users
from services.user_service import UserService
from services.auth_service import AuthorizationService


async def tokeniser(
    user: Users,
    auth_service: AuthorizationService,
    user_service: UserService,
    log_in: bool = None,
):
    access_token = auth_service.create_new_access_token(user.login, "user")
    refresh_token = await auth_service.create_new_refresh_token(user.login)
    acc_time = "continue"
    if log_in:
        acc_time = await user_service.acc_login(user.uuid)

    return {
        "login": user.login,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "login_time": acc_time,
    }
