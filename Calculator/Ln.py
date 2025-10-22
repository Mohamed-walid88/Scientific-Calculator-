import math

def calculate_ln_series(x):
    y = float(x - 1)
    result = y
    term = y

    for i in range(1, 11):
        term *= -y
        result += term / (i + 1)

    return result

def calculate_ln(x):
    if x <= 0:
        raise ValueError('x must be positive')

    if x < 1:
        return -calculate_ln(1 / x)

    n = 0
    y = float(x)

    while y > 1.5:
        y = math.sqrt(y)
        n += 1

    ln_y = calculate_ln_series(y)

    return float((2 ** n) * ln_y)