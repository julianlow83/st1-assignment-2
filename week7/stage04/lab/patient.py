class Patient:
    # this object will represent a patient who registers

    def __init__(self, patient_id: str, full_name: str, phone: str, dob: str, address: str):
        if not patient_id or not full_name or not phone or not dob or not address:
            raise ValueError("Please enter ALL patient fields (ID, Name, Phone, DOB, Address)!")

        self._patient_id = patient_id.strip()
        self._full_name = full_name.strip()
        self._phone = phone.strip()
        self._dob = dob.strip()
        self._address = address.strip()
        self._appointment_history = []

    # getter property (learnt from internet)
    @property
    def patient_id(self) -> str:
        return self._patient_id

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def dob(self) -> str:
        return self._dob

    @property
    def address(self) -> str:
        return self._address

    def update_details(self, phone: str = "", address: str = ""):
        # updates the contact details
        if phone and phone.strip():
            self._phone = phone.strip()
        if address and address.strip():
            self._address = address.strip()

    def add_to_history(self, appointment):
        # will add appointment to the appointment history
        self._appointment_history.append(appointment)

    def get_appointment_history(self) -> list:
        # gets a copy o the appointment history
        return list(self._appointment_history)

    def __repr__(self):
        return f"Patient({self._patient_id}, {self._full_name}, {self._phone})"