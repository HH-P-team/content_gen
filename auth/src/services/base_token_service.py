from abc import ABC, abstractclassmethod


class BaseTokenService(ABC):

    @abstractclassmethod
    async def create_new_access_token(self, data: dict):
        pass

    @abstractclassmethod
    async def create_new_refresh_token(self, token: str):
        pass

    @abstractclassmethod
    async def check_refresh_token(self, refresh_token: str):
        pass

    @abstractclassmethod
    async def check_access_token(self, acces_token: str):
        pass

    @abstractclassmethod
    async def logout(self, login, access_token):
        pass
