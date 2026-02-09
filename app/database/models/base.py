from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Родительский класс для всех таблицы базы данных"""

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
