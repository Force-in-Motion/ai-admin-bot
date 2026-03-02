

from app.database.models.executor import Executor
from app.database.repositories.base import BaseRepo


class ExecutorRepo(BaseRepo[Executor]):
    """ Репозиторий, работающий с моделью Executor """

    model = Executor