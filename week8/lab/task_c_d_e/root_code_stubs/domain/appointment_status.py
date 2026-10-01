from enum import Enum

class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    ARRIVED = "ARRIVED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"