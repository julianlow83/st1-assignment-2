# SmartCare Clinic Appointment Booking System
## Candidate Classes and Relationships (Confirmed Requirements Only)

### Source
Case Study: Assignment_2_Case_Study_S2_2026.docx 【1-4e4fcb】

---

# Confirmed Requirements

| Requirement ID | Requirement |
|---------------|-------------|
| R1 | The system shall manage patients. |
| R2 | The system shall manage practitioners (GPs). |
| R3 | The system shall manage appointments. |
| R4 | The system shall support appointment booking and prevent duplicate appointment bookings. |
| R5 | The system shall maintain appointment status information consistently. |
| R6 | The system shall provide visibility of practitioner availability. |
| R7 | The system shall support appointment cancellation. |
| R8 | The system shall maintain appointment history. |

**Evidence:** The case study states that management wants an initial system to support patient, practitioner and appointment management and identifies issues including duplicate bookings, inconsistent appointment status information, limited visibility of practitioner availability, manual cancellation processes and lack of reliable appointment history. 【1-4e4fcb】

---

# Candidate Classes

## 1. Patient

### Supported Requirements
- R1

### Suggested Attributes
- patientId
- firstName
- lastName
- phoneNumber
- email

### Justification
The system must support patient management. 【1-4e4fcb】

---

## 2. Practitioner

### Supported Requirements
- R2
- R6

### Suggested Attributes
- practitionerId
- name
- availabilityStatus

### Justification
The system must manage practitioners and provide visibility of practitioner availability. 【1-4e4fcb】

---

## 3. Appointment

### Supported Requirements
- R3
- R4
- R5
- R7
- R8

### Suggested Attributes
- appointmentId
- appointmentDateTime
- status
- bookingDate

### Justification
The system must manage appointments, support booking, maintain appointment status, allow cancellations and preserve appointment history. 【1-4e4fcb】

---

# Relationships

## Relationship 1: Patient - Appointment

### Multiplicity

```text
Patient (1) ----------- (0..*) Appointment
```

### Meaning

- A patient may have many appointments.
- Each appointment belongs to exactly one patient.

### Supported Requirements

- R1 Patient management
- R3 Appointment management
- R8 Appointment history

### Justification

Appointment history can only be maintained if appointments are associated with patients. 【1-4e4fcb】

---

## Relationship 2: Practitioner - Appointment

### Multiplicity

```text
Practitioner (1) ----------- (0..*) Appointment
```

### Meaning

- A practitioner may have many appointments.
- Each appointment is scheduled with exactly one practitioner.

### Supported Requirements

- R2 Practitioner management
- R3 Appointment management
- R6 Practitioner availability
- R8 Appointment history

### Justification

The clinic schedules appointments with healthcare practitioners and requires visibility of practitioner availability. 【1-4e4fcb】

---

# UML Class Diagram (Conceptual)

```text
+-----------+
|  Patient  |
+-----------+
      1
      |
      |
      | 0..*
+----------------+
|  Appointment   |
+----------------+
      |
      |
      | 0..*
      |
      1
+---------------+
| Practitioner  |
+---------------+
```

---

# Traceability Matrix

| UML Element | Supporting Requirement(s) |
|------------|---------------------------|
| Patient | R1 |
| Practitioner | R2, R6 |
| Appointment | R3, R4, R5, R7, R8 |
| Patient-Appointment Relationship | R1, R3, R8 |
| Practitioner-Appointment Relationship | R2, R3, R6, R8 |

---

# Excluded Classes

The following classes should **not** be included at this stage because they are not explicitly stated in the case study requirements:

- MedicalRecord
- Consultation
- Prescription
- Payment
- Invoice
- Receptionist
- UserAccount
- AvailabilitySchedule
- Report

Including these classes would introduce assumptions rather than modelling confirmed requirements. 【1-4e4fcb】

---

# Final Recommendation

Use the following three classes only:

1. Patient
2. Practitioner
3. Appointment

With the following relationships:

- Patient (1) ↔ Appointment (0..*)
- Practitioner (1) ↔ Appointment (0..*)

This model is fully traceable to the confirmed requirements in Assignment_2_Case_Study_S2_2026.docx and avoids introducing unverified assumptions. 【1-4e4fcb】