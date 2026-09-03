# list to store all the appointments, which will be dictionaries in the list
appointments = []

#Two functions, one for a new booking and another displaying the bookings and assign them to a menu (from last semester's IIT Python assignment)
def book(patient_name, doctor_name, appt_time):
    # creates the appointment and adds to the list above

    appointment = {
        "patient": patient_name,
        "practitioner": doctor_name,
        "time": appt_time,
                    }

    appointments.append(appointment)
    print(f"\nAppointment successfully booked for {patient_name}!")
    return True


def display():
    #Displays the appointments in the list
    print("CURRENT APPOINTMENTS")

    if not appointments:
        print("No appointments recorded yet.")
    else:
        for index, appt in enumerate(appointments, start=1):
            print(
                f"{index}. Patient: {appt['patient']} | Practitioner: {appt['practitioner']} | Time: {appt['time']}"
            )

def main():
    print("Welcome to SmartCare Appointment Booking System!")

    # Input the 2 patients from the lab notes
    book("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
    book("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

    # Creates the menu (from last semester's IIT Python assignment)
    while True:
        print("\n--- MENU ---")
        print("1. Book New Appointment")
        print("2. View All Appointments")
        print("3. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            print("\n--- New Appointment ---")
            p_name = input("Enter patient name: ")
            dr_name = input("Enter attending Doctor: ")
            appt = input("Enter date and time (e.g., 2024-07-20 02:00 PM): ")

            book(p_name, dr_name, appt)

        elif choice == "2":
            display()

        elif choice == "3":
            print("\nExiting System")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the program
main()