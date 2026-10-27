# hello_module

A minimal, typed Python greeting module, expanded from the original stub:

```python
def hello(): pass
```

## Features

- **Type hints** — fully annotated function and result dataclass
- **Docstrings** — Google-style with examples
- **Tests** — pytest suite covering defaults, custom names, excited tone, edge cases
- **Immutable result** — `HelloResult` frozen dataclass

## Quick start

```bash
pip install -e .
pytest
```

## Example

```python
from hello_module import hello

result = hello("World", excited=True)
print(result.message)  # Hello, World!
```
