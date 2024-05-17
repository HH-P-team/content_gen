from http import HTTPStatus
from functools import wraps

from services.user_service import UserService
from services.role_service import RoleService
from services.auth_service import AuthorizationService
from services.jwt_service import JwtService
from db.pg_user_tools import PgUserStoreTools
from db.pg_role_tools import PgRoleStoreTools
from db.redis import RedisRepository
from helpers.exceptions import AuthException


def roles_required(access_level: int):
    def decorator(function):
        @wraps(function)
        async def wrapper(*args, **kwargs):

            access_token = kwargs.get('common').body.access_token

            user_db = PgUserStoreTools()
            role_db = PgRoleStoreTools()
            redis = RedisRepository()
            jwt = JwtService()
            auth_db = AuthorizationService(jwt, redis)
            role_service = RoleService(role_db)
            user_service = UserService(user_db, auth_db)

            login, role_uuid = await auth_db.check_access_token(access_token)

            if not login:
                raise AuthException(
                    'This operation is forbidden for you',
                    status_code=HTTPStatus.FORBIDDEN,
                )

            user = await user_service.get_user(login)

            if not user:
                raise AuthException(
                    'This operation is forbidden for you',
                    status_code=HTTPStatus.FORBIDDEN,
                )

            role = await role_service.get_role(role_uuid)

            if not role:
                raise AuthException(
                    'A user with these rights was not found',
                    status_code=HTTPStatus.FORBIDDEN,
                )
            elif role.level < access_level:
                raise AuthException(
                    'You do not have enough rights for this function',
                    status_code=HTTPStatus.FORBIDDEN,
                )

            return await function(*args, **kwargs)
        return wrapper
    return decorator
