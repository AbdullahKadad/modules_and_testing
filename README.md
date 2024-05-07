# Factorial Functions

This repository contains two functions for calculating the factorial of a positive integer:

1. `factorial_iterative`: Calculates the factorial of a positive integer using iteration.
2. `factorial_recursion`: Calculates the factorial of a positive integer using recursion.

## Installation

`pip install -r req.txt`

## Usage

### `factorial_iterative`

```python
from factorial_module.factorial_module import (
    factorial_iterative,
    factorial_recursion,
)

result = factorial_iterative(5)
print(result)  # Output: 120

result = factorial_recursion(5)
print(result)  # Output: 120
