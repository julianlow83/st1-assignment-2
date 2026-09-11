

1. **NFR-01 (Usability):** The user interface shall be simple and intuitive, allowing a new receptionist to successfully book, modify, or search for an appointment within 15 minutes of training.
2. **NFR-02 (Data Integrity):** The system shall strictly enforce data validation on all inputs, for example, preventing duplicate patient IDs and invalid time formats.
3. **NFR-03 (Maintainability):** The code shall follow PEP 8 standards, so that future developers can update components without breaking the existing logic.
4. **NFR-04 (Reliability):** The system shall handle user input errors and invalid selections gracefully without crashing ande able to return clear error messages to the user.
5. **NFR-05 (Testability):** The core logic (e.g. timeslot conflict detection and record filtering) shall be split into functions that can be tested independently.