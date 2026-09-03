__COPILOT COMPARISON__

| Question | Human Version | AI Version |
| :--- | :--- | :--- |
| **Easy to understand?** | Variable/function/method naming not as good as Copilot | Copilot's naming more intuitive |
| **Runs successfully?** | Yes (About the same as Copilot) | Yes |
| **Uses only required features?** | Yes (About the same as Copilot) | Yes |
| **Adds assumptions?** | Yes (About the same as Copilot) | Yes |
| **Handles errors?** | No exception handling as it hasn't been taught yet | No (lab says to keep it beginner-friendly when prompting, so it didn't do handling) |
| **Could I explain it?** | Yes, definitely | Yes, Copilot's naming is more intuitive than mine |


__INPUT / OUTPUT TESTING__

| Test Scenario | Inputs Provided                                                                               | Expected Outcome                                                         | Actual Result                                                              |
| :--- |:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| **Normal appointment** | `patient="Eve Six"`<br>`doctor="Dr. John Doe"`<br>`time="2026-10-15 10:00 AM"`                | Appointment added successfully and displayed in list.                    | Appointment added successfully and displayed in list.                      |
| **Blank patient name** | `patient=""`<br>`doctor="Dr. John Doe"`<br>`time="2026-10-15 10:00 AM"`                       | Appointment is still saved as we haven't covered exception handling yet. | Appointment is still saved as we haven't covered exception handling yet.   |
| **Double booking** | `patient="Bob"`<br>`doctor="Dr. John Doe"`<br>`time="2026-10-15 10:00 AM"` *(duplicate time)* | Appointment is still saved as we don't know how to handle double bookings.                       | Appointment is still saved as we don't know how to handle double bookings. | 
| **`NoneType` inputs** | `patient=None`<br>`doctor="Dr. John Doe"`<br>`time=None`                                      | Appointment is still saved as we haven't covered exception handling yet.     |  Appointment is still saved as we haven't covered exception handling yet.                                                                          |