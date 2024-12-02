from dataclasses import dataclass


@dataclass(frozen=True)
class Error:
    """
    A class representing an error with a message.

    Attributes:
        message (str): The error message.
    """

    message: str
