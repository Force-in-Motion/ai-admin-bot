from app.database.models.service import Service
from app.database.repositories.base import BaseRepo


class ServiceRepo(BaseRepo[Service]):
    """ Репозиторий, работающий с моделью Service """

    model = Service