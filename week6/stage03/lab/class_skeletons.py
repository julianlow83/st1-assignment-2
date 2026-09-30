class Patient:
    def __init__(self, patient_id: str, full_name: str, phone: str, dob: str, address: str):
        self.patient_id = patient_id
        self.full_name = full_name
        self.phone = phone
        self.dob = dob
        self.address = address

    def register_patient(self) -> bool:
        pass

    def update_details(self, phone: str, address: str):
        pass

    def get_appointment_history(self) -> list:
        pass


class Practitioner:
    def __init__(self, practitioner_id: str, doctor_name: str, speciality: str, room_number: str):
        self.practitioner_id = practitioner_id
        self.doctor_name = doctor_name
        self.speciality = speciality
        self.room_number = room_number

    def add_practitioner(self) -> bool:
        pass

    def get_daily_schedule(self, date: str) -> list:
        pass

    def check_availability(self, date_time: str) -> bool:
        pass


class Appointment:
    def __init__(self, appointment_id: str, patient_id: str, practitioner_id: str, date_time: str):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.practitioner_id = practitioner_id
        self.date_time = date_time
        self.status = "Scheduled"
        self.cancellation_reason = ""

    def create_booking(self, patient_id: str, doc_id: str, date_time: str) -> bool:
        pass

    def check_collision(self, doc_id: str, date_time: str) -> bool:
        pass

    def update_status(self, new_status: str):
        pass

    def cancel_appointment(self, reason: str):
        pass