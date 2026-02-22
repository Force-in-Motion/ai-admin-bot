from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base
from app.tools.types import AppointmentStatus


if TYPE_CHECKING:
    from app.database.models import Client, Executor


class Appointment(Base):

    __tablename__ = "appointments"

    # Мастер + Время должны быть уникальны, клиентт + время должны быть уникальны
    __table_args__ = (
        UniqueConstraint("executor_id", "start_time", name="executor_appointment_uniq"),
        UniqueConstraint("client_id", "start_time", name="client_appointment_uniq"),
    )

    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.id"),
        nullable=False,
    )

    executor_id: Mapped[int] = mapped_column(
        ForeignKey("executors.id"),
        nullable=False,
    )

    service_id: Mapped[int] = mapped_column(
        ForeignKey("services.id"),
        nullable=False,
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    end_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        Enum(AppointmentStatus),
        default="planned",
    )

    client: Mapped["Client"] = relationship(
        back_populates="appointments",
        lazy="select",
        uselist=False,
    )

    executor: Mapped["Executor"] = relationship(
        back_populates="appointments",
        lazy="select",
        uselist=False,
    )
