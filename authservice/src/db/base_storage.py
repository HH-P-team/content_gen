from abc import ABC, abstractmethod


class BaseUserStore(ABC):
    @abstractmethod
    async def get_user(self, *args, **kwargs):
        pass

    @abstractmethod
    async def create_user(self, *args, **kwargs):
        pass

    @abstractmethod
    async def update_user(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_user_by_uuid(self, *args, **kwargs):
        pass


class BaseAccStore(ABC):
    @abstractmethod
    async def add_acc(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_acc_table(self, *args, **kwargs):
        pass


class BaseAsyncCache(ABC):
    @abstractmethod
    async def get(self, *args, **kwargs):
        pass

    @abstractmethod
    async def set(self, *args, **kwargs):
        pass

    @abstractmethod
    async def delete(self, *args, **kwargs):
        pass

    @abstractmethod
    async def key_by_pattern(self, *args, **kwargs):
        pass
