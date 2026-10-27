"""
Core greeting logic for hello_module.

Provides the `hello` function, which returns a friendly greeting string.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class HelloResult:
    """The result of a greeting invocation."""

    recipient: str
    salutation: str
    message: str


def hello(name: str = "World", *, excited: bool = False) -> HelloResult:
    """Return a friendly greeting for the given *name*.

    Args:
        name: The person or entity to greet. Defaults to "World".
        excited: Whether to use an enthusiastic tone (ending with ``!``).
                 Defaults to ``False``.

    Returns:
        A ``HelloResult`` dataclass containing the recipient, salutation,
        and the composed greeting message.

    Example:
        >>> result = hello("Alice")
        >>> result.message
        'Hello, Alice.'
        >>> hello("Bob", excited=True).message
        'Hello, Bob!'
    """
    sanitised = str(name).strip()
    if not sanitised:
        sanitised = "World"

    salutation = "Hello"
    punctuation = "!" if excited else "."
    message = f"{salutation}, {sanitised}{punctuation}"

    return HelloResult(
        recipient=sanitised,
        salutation=salutation,
        message=message,
    )
