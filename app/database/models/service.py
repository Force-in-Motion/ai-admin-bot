from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models import Base, TimestampMixin


if TYPE_CHECKING:
    from app.database.models.executor import Executor


class Service(Base, TimestampMixin):

    __tablename__ = "services"

    executor_id: Mapped[int] = mapped_column(
        ForeignKey("executors.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Цена в копейках
    price: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    # Длительность услуги в минутах
    duration: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=60,
    )

    executor: Mapped["Executor"] = relationship(
        back_populates="services",
        lazy="select",
        uselist=False,
    )
