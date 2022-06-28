from abc import ABCMeta, abstractmethod

class IRepository(metaclass=ABCMeta):

    @abstractmethod
    async def get_list_async(self):
        raise NotImplementedError

    @abstractmethod
    async def get_async(self, id):
        raise NotImplementedError

    @abstractmethod
    async def add_async(self, kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_async(self, id):
        raise NotImplementedError

    @abstractmethod
    async def update_async(self, id):
        raise NotImplementedError