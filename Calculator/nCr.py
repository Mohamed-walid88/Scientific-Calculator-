import Factorial

def calculate_ncr(n, r):
    if r > n:
        raise ValueError('r is greater than n')
    if r == 0 or r == n:
        return 1
    return Factorial.calculate_factorial(n) / (Factorial.calculate_factorial(r) * Factorial.calculate_factorial(n - r))
