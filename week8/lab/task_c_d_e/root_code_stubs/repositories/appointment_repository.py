from abc import ABC, abstractmethod
from typing import List, Optional
from domain.appointment import Appointment

class IAppointmentRepository(ABC):
    """
    Abstract contract for Appointment persistence.
    Contains ONLY the methods required for active use cases.
    """
    @abstractmethod
    def save(self, appointment: Appointment) -> None:
        """Persist a new or updated appointment."""
        pass

    @abstractmethod
    def find_by_id(self, appointment_id: str) -> Optional[Appointment]:
        """Retrieve an appointment by its unique ID."""
        pass

    @abstractmethod
    def find_by_practitioner(self, practitioner_id: str) -> List[Appointment]:
        """Retrieve all appointments booked for a specific practitioner."""
        pass