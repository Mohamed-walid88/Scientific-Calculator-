import Factorial

def calculate_npr(n, r):
    if r > n:
        raise ArithmeticError("invalid input")

    return Factorial.calculate_factorial(n) / Factorial.calculate_factorial(n - r)