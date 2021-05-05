class IncorrectImplementingClass(Exception):
    """
    Raised if a concrete implementation does not satisfy
    the requirements of an abstract class.

    Parameters
    ----------
    implementing_class : class
        A concrete class implementing an abstract class.

    message: str, optional
        Overrides the exception's message.
        
    reason: str, optional
        Appended at the end of error message, can be used
        to explain why the exception was thrown.
    """

    def __init__(self, *, implementing_class, message="", reason=""):
        self.message = (
            message
            if message
            else f"Class {str(implementing_class)} cannot correctly extend the abstract class"
        )
        if reason:
            self.message = f"{self.message}: {reason}"
        super().__init__(self.message)
