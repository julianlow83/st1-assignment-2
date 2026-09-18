# SmartCare System Analysis: Concepts, Requirements, State & Behaviour

## 1. Candidate Concepts

* **Patient:** Individuals receiving care. Holds personal details and visit histories.
* **Doctor:** Medical staff conducting consultations. Holds specialty details and availability.
* **Appointment:** Represents the scheduled time block linking a Patient and a Doctor.
* **Schedule / Availability:** Represents a doctor's working hours and free/booked time slots.
* **Appointment History:** Archive of past completed, cancelled, or missed patient visits.
* **Operational Report:** Summary data generated for management (e.g., daily booking counts, cancellation rates).
---

## 2. Supporting Requirements

* **Search & Retrieval:** The system must support searching for patient records by name or contact details to avoid duplicate patient entries.
* **Conflict Prevention:** Must validate practitioner schedules before saving an appointment to ensure no overlapping bookings.
* **Status Tracking:** Every appointment record must support a state update (e.g., *Scheduled*, *Completed*, *Cancelled*).
* **Audit Trail:** Completed or cancelled appointments must be saved persistently rather than hard-deleted.
* **Reporting Output:** System must compile simple operational metrics on demand for clinic management.
---

## 3. System State

### Patient State
* **Unregistered:** Patient does not exist in the system.
* **Registered / Active:** Patient profile exists and can be linked to new appointments.

### Practitioner State
* **Available:** Practitioner has free time slots open for a consult.
* **Full:** Practitioner has no open time slots for a given time period.

### Appointment State
* **Scheduled:** Appointment is created and confirmed for a future time.
* **Arrived / In Progress:** Patient has checked in at reception for their consult.
* **Completed:** Consultation is finished successfully.
* **Cancelled:** Booking was terminated prior to consultation (requires recording a cancellation reason).

---

## 4. System Behaviour

* **`register_patient()`:** Accepts input, validates mandatory fields, and stores a new patient record.
* **`search_patient()`:** Filters existing patient records based on partial/exact query inputs.
* **`check_availability()`:** Checks a doctor's schedule against a date/time slot to detect a collision.
* **`create_appointment()`:** Links an existing patient, doctor, and time slot after performing a conflict check.
* **`update_status()`:** Transitions an appointment's lifecycle state (e.g., from *Scheduled* to *Cancelled*).
* **`generate_report()`:** Iterates over stored appointment records to display a summary for management.