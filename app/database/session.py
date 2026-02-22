from contextlib import asynccontextmanager
from typing import AsyncGenerator, AsyncIterator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from app.core.config import db_settings


class DBConnector:
    def __init__(self, url: str, echo: bool):

        self.__engine = create_async_engine(url=url, echo=echo)

        self.__session_factory = async_sessionmaker(
            bind=self.__engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Асинхронный генератор, который предоставляет сессию для FastAPI-маршрутов, автоматически закрывает её после использования и возвращает ее в пул соединений.
        :return: AsyncSession
        """
        async with self.__session_factory() as session:
            yield session

    @asynccontextmanager
    async def session_scope(self) -> AsyncIterator[AsyncSession]:
        """
        Асинхронный контекстный менеджер, который предоставляет сессию для фоновых задач и автоматически закрывает её после использования.
        :return: AsyncSession
        """
        async with self.__session_factory() as session:
            yield session


db_connector = DBConnector(url=db_settings.url, echo=db_settings.echo)
