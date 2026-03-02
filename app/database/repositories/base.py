from typing import Any, Generic, Type, Optional
from sqlalchemy import select, delete, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.tools.types import DBModel
from app.interface.repository import ARepo
from app.tools.exeptions import DatabaseError


class BaseRepo(Generic[DBModel], ARepo):

    model: Type[DBModel]

    @classmethod
    async def get_all(
        cls,
        session: AsyncSession,
        **kwargs: Any,
    ) -> list[DBModel]:
        """
        Получает список конкретных ORM моделей согласно переданным аргументам
        :param session: Объект асинхронной сессии
        :param kwargs: Именованные аргументы для фильтрации данных
        :return: Список ORM моделей
        """
        try:
            stmt = select(cls.model).filter_by(**kwargs)

            result = await session.execute(stmt)

            return list(result.scalars().all())

        except SQLAlchemyError as e:
            raise DatabaseError(f"Error when receiving all {cls.model.__name__}s") from e

    @classmethod
    async def get_one(
        cls,
        session: AsyncSession,
        **kwargs: Any,
    ) -> Optional[DBModel]:
        """
        Получает конкретную ORM модель согласно переданным аргументам
        :param session: Объект асинхронной сессии
        :param kwargs: Именованные аргументы для фильтрации данных
        :return: ORM модель
        """
        try:
            stmt = select(cls.model).filter_by(**kwargs)

            result = await session.execute(stmt)

            return result.scalar_one_or_none()

        except SQLAlchemyError as e:
            raise DatabaseError(f"Error when receiving {cls.model.__name__}") from e

    @classmethod
    async def add(
        cls,
        model: DBModel,
        session: AsyncSession,
    ) -> DBModel:
        """
        Добавляет ORM модель в конкретную таблицу БД
        :param model: ORM модель
        :param session: Объект асинхронной сессии
        :return: ORM модель, добавленную в БД
        """
        try:
            session.add(model)

            await session.commit()

            await session.refresh(model)

            return model

        except SQLAlchemyError as e:
            await session.rollback()
            raise DatabaseError(f"Error when adding {cls.model.__name__}") from e

    @classmethod
    async def update(
        cls,
        model: DBModel,
        new_data: dict,
        session: AsyncSession,
    ) -> DBModel:
        """
        Изменяет конкретную ORM модель в БД
        :param model: Измененную ORM модель
        :param session: Объект асинхронной сессии
        :return: Измененную ORM модель
        """
        try:
            for key, value in new_data.items():
                setattr(model, key, value)

            await session.commit()

            await session.refresh(model)

            return model

        except SQLAlchemyError as e:
            await session.rollback()
            raise DatabaseError(f"Error when updating {cls.model.__name__}") from e

    @classmethod
    async def delete(
        cls,
        model: DBModel,
        session: AsyncSession,
    ) -> DBModel:
        """
        Удаляет конкретную ORM модель из БД
        :param model: ORM модель, переданную для удаления
        :param session: Объект асинхронной сессии
        :return: Удаленную ORM модель
        """
        try:
            session.delete(model)

            await session.commit()

            return model

        except SQLAlchemyError as e:
            await session.rollback()
            raise DatabaseError(f"Error when deleting {cls.model.__name__}") from e

    @classmethod
    async def delete_all(
        cls,
        session: AsyncSession,
        **kwargs: Any,
    ) -> list:
        """
        Удаляет все модели таблицы, согласно переданным аргументам
        :param session: Объект асинхронной сессии
        :param kwargs: Именованные аргументы для фильтрации данных
        :return: Пустой список
        """
        try:
            stmt = delete(cls.model).filter_by(**kwargs)

            await session.execute(stmt)

            await session.commit()

            return []

        except SQLAlchemyError as e:
            await session.rollback()
            raise DatabaseError(f"Error when deleting all {cls.model.__name__}s") from e

    @classmethod
    async def clear(
        cls,
        session: AsyncSession,
    ) -> list:
        """
        Полностью очищает таблицу
        :param session: Объект асинхронной сессии
        :return: Пустой список
        """
        try:
            table_name = cls.model.__tablename__

            stmt = text(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE")

            await session.execute(stmt)

            await session.commit()

            return []

        except SQLAlchemyError as e:
            await session.rollback()
            raise DatabaseError(f"Error when clearing table {cls.model.__name__}") from e
