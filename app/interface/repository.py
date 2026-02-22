from abc import abstractmethod, ABC


class ARepo(ABC):

    @abstractmethod
    async def get_all_models(*args, **kwargs):
        pass

    @abstractmethod
    async def get_model(*args, **kwargs):
        pass

    @abstractmethod
    async def add(*args, **kwargs):
        pass

    @abstractmethod
    async def update(*args, **kwargs):
        pass

    @abstractmethod
    async def delete(*args, **kwargs):
        pass

    @abstractmethod
    async def delete_all(*args, **kwargs):
        pass
