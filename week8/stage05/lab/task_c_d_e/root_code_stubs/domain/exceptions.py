class DomainException(Exception):
    """This is thebase exception for all core business domain errors."""
    pass

class AppointmentException(DomainException):
    """Will be raised when an appointment invariant or state transition is violated."""
    pass