from app.database.models.client import Client
from app.database.repositories.base import BaseRepo


class ClientRepo(BaseRepo[Client]):
    """ Репозиторий, работающий с моделью Client """
    
    model = Client