from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models import Base, TimestampMixin, UserDataMixin


if TYPE_CHECKING:
    from app.database.models import Appointment


class Client(Base, TimestampMixin, UserDataMixin):

    __tablename__ = "clients"

    comments: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    appointments: Mapped[List["Appointment"]] = relationship(
        back_populates="client",
        lazy="select",
        uselist=True,
    )
