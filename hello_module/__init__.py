"""
hello_module — A simple greeting module.

This package provides a configurable greeting function that supports
custom names, salutations, and emphasis levels.
"""

from .core import hello, HelloResult

__all__ = ["hello", "HelloResult"]
