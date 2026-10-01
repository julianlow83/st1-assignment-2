from typing import Optional
from domain.appointment import Appointment, AppointmentStatus
from domain.exceptions import AppointmentException
from repositories.appointment_repository import IAppointmentRepository

class AppointmentService:
    """
    THIS SATISFIES TASK D (I think?! It's quite vague)
    The Workflow Orchestrator / Application Service.
    Coordinates use cases and repositories without stealing domain behavior
    """
    def __init__(self, repository: IAppointmentRepository):
        # Constructor Dependency Injection of Repository Contract
        self._repository = repository

    def book_appointment(
        self,
        appointment_id: str,
        patient_id: str,
        practitioner_id: str,
        date_time: str
    ) -> Appointment:
        # Step 1 Fetch existing bookings for practitioner to check collisions
        existing_bookings = self._repository.find_by_practitioner(practitioner_id)
        
        # Step 2 Delegate collision rule validation to Appointment domain logic
        if self._repository.find_by_id(appointment_id):
            raise AppointmentException(f"Appointment ID '{appointment_id}' already exists.")

        # Step 3 Replaces direct constructor call in AppointmentService.book_appointment (from TASK G)
        new_appointment = Appointment.create_booking(
            appointment_id=appointment_id,
            patient_id=patient_id,
            practitioner_id=practitioner_id,
            date_time=date_time
        )

        # Step 4. Persist via repository interface
        self._repository.save(new_appointment)
        return new_appointment