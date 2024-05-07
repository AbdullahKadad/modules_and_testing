def factorial_iterative(n):
    """
    Calculate the factorial of a positive integer using iteration.

    Parameters:
    n (int): The integer for which factorial is to be calculated.

    Returns:
    int: The factorial of n.
    str: If n is a negative number.
    """
    if n < 0:
        return "Factorial is undefined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursion(n):
    """
    Calculate the factorial of a positive integer using recursion.

    Parameters:
    n (int): The integer for which factorial is to be calculated.

    Returns:
    int: The factorial of n.
    str: If n is a negative number.
    """
    if n < 0:
        return "Factorial is undefined for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)
