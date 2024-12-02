from dataclasses import dataclass, field
import typing as t

from .error import Error


@dataclass(frozen=True)
class Result:
    """
    A class representing the result of an operation, which can be either a success or a failure.

    Attributes:
        __value (t.Any): The value of a successful result.
        __error (t.Optional[Error]): The error message of a failed result.
    """

    __value: t.Any = field(default=None, init=False)
    __error: t.Optional[Error] = field(default=None, init=False)

    @staticmethod
    def success(value: t.Any) -> "Result":
        """
        Creates a Result object representing a successful operation.

        Args:
            value (t.Any): The value of the successful result.

        Returns:
            Result: A Result object containing the success value.
        """
        result = Result()
        object.__setattr__(result, "_Result__value", value)
        return result

    @staticmethod
    def failure(message: str) -> "Result":
        """
        Creates a Result object representing a failed operation.

        Args:
            message (str): The error message of the failed result.

        Returns:
            Result: A Result object containing the error message.
        """
        result = Result()
        object.__setattr__(result, "_Result__error", Error(message))
        return result

    def has_error(self) -> bool:
        """
        Checks if the Result object represents a failed operation.

        Returns:
            bool: True if the Result object contains an error, False otherwise.
        """
        return self.__error is not None

    @property
    def value(self) -> t.Any:
        """
        Gets the value of a successful result.

        Returns:
            t.Any: The value of the successful result.
        """
        return self.__value

    @property
    def error(self) -> t.Optional[Error]:
        """
        Gets the error message of a failed result.

        Returns:
            t.Optional[Error]: The error message of the failed result.
        """
        return self.__error
