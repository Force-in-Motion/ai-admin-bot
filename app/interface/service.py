from abc import abstractmethod, ABC


class AService(ABC):

    @abstractmethod
    async def get_all_models(*args, **kwargs):
        pass

    @abstractmethod
    async def get_model(*args, **kwargs):
        pass

    @abstractmethod
    async def create_model(*args, **kwargs):
        pass

    @abstractmethod
    async def update_model(*args, **kwargs):
        pass

    @abstractmethod
    async def delete_model(*args, **kwargs):
        pass

    @abstractmethod
    async def delete_all_models(*args, **kwargs):
        pass