#'AI On' activity, made with Copilot

from __future__ import annotations

from AppointmentStatus import AppointmentStatus
from AppointmentException import AppointmentException


class Appointment:
    """
    Connects one Patient to one Practitioner at a scheduled date/time.
    """

    ACTIVE_STATUSES = {
        AppointmentStatus.SCHEDULED,
        AppointmentStatus.ARRIVED,
        AppointmentStatus.IN_PROGRESS,
    }

    ALLOWED_TRANSITIONS = {
        AppointmentStatus.SCHEDULED: {
            AppointmentStatus.ARRIVED,
            AppointmentStatus.CANCELLED,
        },
        AppointmentStatus.ARRIVED: {
            AppointmentStatus.IN_PROGRESS,
            AppointmentStatus.CANCELLED,
        },
        AppointmentStatus.IN_PROGRESS: {
            AppointmentStatus.COMPLETED,
            AppointmentStatus.CANCELLED,
        },
        AppointmentStatus.COMPLETED: set(),
        AppointmentStatus.CANCELLED: set(),
    }

    def __init__(
        self,
        appointment_id: str,
        patient_id: str,
        practitioner_id: str,
        date_time: str,
        status: AppointmentStatus = AppointmentStatus.SCHEDULED,
        cancellation_reason: str = "",
    ) -> None:
        if not appointment_id or not appointment_id.strip():
            raise AppointmentException("Appointment ID is required.")
        if not patient_id or not patient_id.strip():
            raise AppointmentException("Appointment must reference a patient.")
        if not practitioner_id or not practitioner_id.strip():
            raise AppointmentException("Appointment must reference a practitioner.")
        if not date_time or not date_time.strip():
            raise AppointmentException("Appointment must specify a date and time.")

        self._appointment_id = appointment_id.strip()
        self._patient_id = patient_id.strip()
        self._practitioner_id = practitioner_id.strip()
        self._date_time = date_time.strip()
        self._status = status
        self._cancellation_reason = cancellation_reason.strip()

        # Validation check (after _cancellation_reason is stripped)
        if self._status == AppointmentStatus.CANCELLED and not self._cancellation_reason:
            raise AppointmentException("Cancellation reason is required for cancelled appointments.")

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient_id(self) -> str:
        return self._patient_id

    @property
    def practitioner_id(self) -> str:
        return self._practitioner_id

    @property
    def date_time(self) -> str:
        return self._date_time

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    @property
    def cancellation_reason(self) -> str:
        return self._cancellation_reason

    @classmethod
    def create_booking(
        cls,
        appointment_id: str,
        patient_id: str,
        practitioner_id: str,
        date_time: str,
        existing_appointments: list["Appointment"],
    ) -> "Appointment":
        if cls.check_collision(practitioner_id, date_time, existing_appointments):
            raise AppointmentException(
                "Practitioner already has an active appointment at that time."
            )

        return cls(
            appointment_id=appointment_id,
            patient_id=patient_id,
            practitioner_id=practitioner_id,
            date_time=date_time,
        )

    @staticmethod
    def check_collision(
        practitioner_id: str,
        date_time: str,
        existing_appointments: list["Appointment"],
    ) -> bool:
        for appointment in existing_appointments:
            if (
                appointment.practitioner_id == practitioner_id
                and appointment.date_time == date_time
                and appointment.is_active()
            ):
                return True
        return False

    def update_status(self, new_status: AppointmentStatus) -> None:
        """Updates status along allowed lifecycle transitions (excluding cancellation)."""
        if not isinstance(new_status, AppointmentStatus):
            raise AppointmentException("Invalid appointment status.")

        if new_status == AppointmentStatus.CANCELLED:
            raise AppointmentException(
                "Use cancel_appointment(reason) to cancel an appointment."
            )

        allowed = self.ALLOWED_TRANSITIONS[self._status]
        if new_status not in allowed:
            raise AppointmentException(
                f"Invalid transition from {self._status.value} to {new_status.value}."
            )

        self._status = new_status

    def cancel_appointment(self, reason: str) -> None:
        """Cancels the appointment and mandates a non-empty cancellation reason."""
        if not reason or not reason.strip():
            raise AppointmentException("Cancellation reason is required.")

        allowed = self.ALLOWED_TRANSITIONS[self._status]
        if AppointmentStatus.CANCELLED not in allowed:
            raise AppointmentException("Appointment cannot be cancelled from its current state.")

        self._status = AppointmentStatus.CANCELLED
        self._cancellation_reason = reason.strip()

    def is_active(self) -> bool:
        return self._status in self.ACTIVE_STATUSES

    def __str__(self) -> str:
        return (
            f"Appointment("
            f"id={self._appointment_id}, "
            f"patient={self._patient_id}, "
            f"practitioner={self._practitioner_id}, "
            f"time={self._date_time}, "
            f"status={self._status.value})"
        )