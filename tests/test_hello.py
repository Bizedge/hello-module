"""Tests for the hello_module package."""

import pytest

from hello_module import hello, HelloResult


class TestHello:
    """Suite of tests for the ``hello`` function."""

    def test_default_greeting(self) -> None:
        """Calling hello() with no arguments greets 'World'."""
        result = hello()
        assert isinstance(result, HelloResult)
        assert result.recipient == "World"
        assert result.message == "Hello, World."

    def test_custom_name(self) -> None:
        """A named greeting includes the provided name."""
        result = hello("Alice")
        assert result.recipient == "Alice"
        assert result.message == "Hello, Alice."

    def test_excited_tone(self) -> None:
        """The excited flag appends an exclamation mark."""
        result = hello("Bob", excited=True)
        assert result.message == "Hello, Bob!"

    def test_empty_name_falls_back_to_world(self) -> None:
        """An empty or whitespace-only name falls back to 'World'."""
        assert hello("").recipient == "World"
        assert hello("   ").recipient == "World"

    def test_dataclass_is_frozen(self) -> None:
        """HelloResult should be immutable."""
        result = hello("Test")
        with pytest.raises(AttributeError):
            result.recipient = "Mutated"  # type: ignore[misc]
