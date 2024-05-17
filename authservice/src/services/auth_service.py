import uuid
from datetime import datetime, timedelta

from fastapi import Depends

from core.settings import settings
from db.base_storage import BaseAsyncCache
from db.redis import RedisRepository
from services.base_token_service import BaseTokenService
from services.jwt_service import JwtService


class AuthorizationService(BaseTokenService):
    def __init__(self, token_service: JwtService, db: BaseAsyncCache):
        self.tokenaser = token_service
        self.db = db

    def create_new_access_token(
        self,
        login: str,
        role: str,
    ):

        expiration_time = datetime.utcnow() + timedelta(
            minutes=settings.access_token_expires_in
        )
        playload = {
            "login": str(login),
            "role": role,
            "exp": expiration_time,
            "type": "access",
        }

        access_token = self.tokenaser.create_token(playload)

        return access_token

    async def create_new_refresh_token(self, login: str):
        time_delta = timedelta(days=settings.refresh_token_expires_in)
        expiration_time = datetime.utcnow() + time_delta
        playload = {"login": login, "exp": expiration_time, "type": "refresh"}

        refresh_token = self.tokenaser.create_token(playload)

        await self.db.set(key=login, value=refresh_token, expire=time_delta)
        return refresh_token

    async def check_refresh_token(self, refresh_token):
        data = self.tokenaser.verify_token(refresh_token)
        if data:
            old_token = await self.db.get(key=data["login"])
            if old_token.decode("utf-8") == refresh_token:
                return data["login"]

    async def check_access_token(self, acces_token):
        data = self.tokenaser.verify_token(acces_token)
        if data:
            exp_time = data["exp"]
            if datetime.fromtimestamp(exp_time) >= datetime.utcnow():
                login = data["login"]
                role = data["role"]
                keys_logaut_tokens = await self.__get_logout_tokens(login)
                for key in keys_logaut_tokens:
                    token = await self.db.get(key=key)
                    if acces_token == token.decode("utf-8"):
                        return None
                return login, role
        return None, None

    async def __add_logout_token(self, token):
        data = self.tokenaser.verify_token(token)
        if data:
            login = data["login"]
            exp_time = data["exp"]
            num = len(await self.__get_logout_tokens(login))
            time_to_remove = (
                datetime.fromtimestamp(exp_time) - datetime.utcnow()
            )

            await self.db.set(
                key=f"{login}:{num}", value=token, expire=time_to_remove
            )

    async def __clean_refresh_token(self, login):

        await self.db.delete(login)

    async def __get_logout_tokens(self, login):
        tokens = await self.db.key_by_pattern(f"{login}:*")
        return tokens

    async def logout(self, login, access_token):
        await self.__add_logout_token(access_token)
        await self.__clean_refresh_token(login)


def get_auth_service(
    db: BaseAsyncCache = Depends(RedisRepository),
    token_service: JwtService = Depends(JwtService),
) -> AuthorizationService:

    return AuthorizationService(token_service, db)
