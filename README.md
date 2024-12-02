# SimpleResult

A simple library for handling operation results with success and error states.

## Installation

```bash
pip install .
```
## Usage

```python
from simpleresult import Result

# Success case
success_result = Result.success(42)
print(success_result.value)  # Output: 42

# Failure case
failure_result = Result.failure("An error occurred")
print(failure_result.error.message)  # Output: An error occurred
```

## License

This project is licensed under the MIT License.
