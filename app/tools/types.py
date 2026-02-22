import enum
from typing import TypeVar, TYPE_CHECKING


if TYPE_CHECKING:
    from pydantic import BaseModel
    from app.interface import ARepo
    from app.database.models import Base


class AppointmentStatus(enum.Enum):

    planned = "planned"  # Запись создана

    confirmed = "confirmed"  # Мастер подтвердил

    completed = "completed"  # Услуга оказана (деньги в кассе)

    cancelled = "cancelled"  # Клиент или мастер отменили

    not_come = "not_come"  # Клиент не пришел


# Абстрактные типы модели, схемы, адаптера
DBModel = TypeVar("DBModel", bound="Base")

Repo = TypeVar("Repo", bound="ARepo")

PDScheme = TypeVar("PDScheme", bound="BaseModel")
