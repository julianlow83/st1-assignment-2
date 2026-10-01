class Practitioner:
    # represents a Doctor at the clinic

    def __init__(self, practitioner_id: str, doctor_name: str, speciality: str, room_number: str):
        if not practitioner_id or not doctor_name or not speciality or not room_number:
            raise ValueError("All practitioner fields are mandatory!")

        self._practitioner_id = practitioner_id.strip()
        self._doctor_name = doctor_name.strip()
        self._speciality = speciality.strip()
        self._room_number = room_number.strip()
        self._assigned_appointments = []

    # getter property (learnt from internet)

    @property
    def practitioner_id(self) -> str:
        return self._practitioner_id

    @property
    def doctor_name(self) -> str:
        return self._doctor_name

    @property
    def speciality(self) -> str:
        return self._speciality

    @property
    def room_number(self) -> str:
        return self._room_number

    def assign_appointment(self, appointment):
        # assigns appointment to the doctors schedule
        self._assigned_appointments.append(appointment)

    def get_daily_schedule(self, date: str) -> list:
        # returns list of appointments for that doctor
        return [
            appt for appt in self._assigned_appointments
            if getattr(appt, 'date_time', '').startswith(date)
        ]

    def __repr__(self):
        return f"Practitioner({self._practitioner_id}, Dr. {self._doctor_name}, {self._speciality}, Room: {self._room_number})"