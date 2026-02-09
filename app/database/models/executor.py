from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Integer, JSON, Text

from app.database.models import Base, TimestampMixin, UserDataMixin


if TYPE_CHECKING:
    from app.database.models import Service, Appointment


class Executor(Base, TimestampMixin, UserDataMixin):  # Исполнитель

    __tablename__ = "executors"

    experience: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    specialization: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    bio: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )

    working_hours: Mapped[dict] = mapped_column(
        JSON,
        server_default="{}",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    services: Mapped[List["Service"]] = relationship(
        back_populates="executor",
        lazy="select",
        uselist=True,
    )

    appointments: Mapped[List["Appointment"]] = relationship(
        back_populates="executor",
        lazy="select",
        uselist=True,
    )
