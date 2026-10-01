### Personal Reflection / CoPilot Experience

When CoPilot went through the stubs, a few quick improvements stood out for the service and repository layers:

1. **Accepted: Use a Domain Factory Method**
Instead of calling `Appointment(...)` directly inside `AppointmentService`, switched to `Appointment.create_booking(...)`. It keeps entity setup where it belongs, inside the domain, so the service doesn't have to worry about default statuses or initial rules.
2. **Modified: Streamline Duplicate ID Checks**
Checking if an appointment ID already exists is a no-brainer, but doing a standalone database call *before* checking practitioner availability felt wasteful. I modified this to handle validation efficiently without making extra, redundant database trips.
3. **Deferred: Row Hydration Enforcement**
Making sure raw SQL rows turn back into proper `Appointment` objects is super important, but tweaking that right now is premature since the repository stub is just a placeholder. Deferred this to Task E integration testing once live SQLite queries are running.