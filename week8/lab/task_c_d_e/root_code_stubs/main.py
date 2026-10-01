import tkinter as tk
from persistence.sqlite_repository import SQLiteAppointmentRepository
from services.appointment_service import AppointmentService
from presentation.gui_view import SmartCareApp


def main():
    # Step 1: Instantiate the concrete infrastructure
    repo = SQLiteAppointmentRepository(db_path="smartcare.db")

    # Step 2: Inject the repository into the application service
    service = AppointmentService(repository=repo)

    # Step 3: Initialize the Tkinter root window
    root = tk.Tk()

    # Step 4: Inject the service into the Tkinter GUI presentation layer
    app_ui = SmartCareApp(root=root, service=service)

    # Step 5: Launch the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()