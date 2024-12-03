from dataclasses import dataclass, field
from typing import Generic, TypeVar, Optional

from .error import Error

T = TypeVar("T")


@dataclass(frozen=True)
class Result(Generic[T]):
    """
    A class representing the result of an operation, which can be either a success or a failure.

    Attributes:
        _value (Optional[T]): The value of a successful result.
        _error (Optional[Error]): The error message of a failed result.
    """

    _value: Optional[T] = field(default=None, init=False)
    _error: Optional[Error] = field(default=None, init=False)

    @staticmethod
    def success(value: T) -> "Result[T]":
        """
        Creates a Result object representing a successful operation.

        Args:
            value (T): The value of the successful result.

        Returns:
            Result[T]: A Result object containing the success value.
        """
        result = Result[T]()
        object.__setattr__(result, "_value", value)
        return result

    @staticmethod
    def failure(message: str) -> "Result[T]":
        """
        Creates a Result object representing a failed operation.

        Args:
            message (str): The error message of the failed result.

        Returns:
            Result[T]: A Result object containing the error message.
        """
        result = Result[T]()
        object.__setattr__(result, "_error", Error(message))
        return result

    def has_error(self) -> bool:
        """
        Checks if the Result object represents a failed operation.

        Returns:
            bool: True if the Result object contains an error, False otherwise.
        """
        return self._error is not None

    @property
    def value(self) -> Optional[T]:
        """
        Gets the value of a successful result.

        Returns:
            Optional[T]: The value of the successful result.
        """
        return self._value

    @property
    def error(self) -> Optional[Error]:
        """
        Gets the error message of a failed result.

        Returns:
            Optional[Error]: The error message of the failed result.
        """
        return self._error
