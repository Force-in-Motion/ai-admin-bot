import enum

class AppointmentStatus(enum.Enum):

    planned = "planned"      # Запись создана
    
    confirmed = "confirmed"  # Мастер подтвердил
    
    completed = "completed"  # Услуга оказана (деньги в кассе)
    
    cancelled = "cancelled"  # Клиент или мастер отменили
    
    not_come = "not_come"      # Клиент не пришел