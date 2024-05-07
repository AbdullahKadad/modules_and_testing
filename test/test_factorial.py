from factorial_module.factorial_module import (
    factorial_iterative,
    factorial_recursion,
)


def test_factorial_iterative_positive():
    assert factorial_iterative(5) == 120
    assert factorial_iterative(0) == 1
    assert factorial_iterative(1) == 1


def test_factorial_iterative_negative():
    actual = factorial_iterative(-1)
    expected = "Factorial is undefined for negative numbers"
    assert expected == actual


def test_factorial_iterative_large_number():
    assert factorial_iterative(10) == 3628800


def test_factorial_recursion_positive():
    assert factorial_recursion(5) == 120
    assert factorial_recursion(0) == 1
    assert factorial_recursion(1) == 1


def test_factorial_recursion_negative():
    actual = factorial_iterative(-1)
    expected = "Factorial is undefined for negative numbers"
    assert expected == actual


def test_factorial_recursion_large_number():
    assert factorial_recursion(10) == 3628800
