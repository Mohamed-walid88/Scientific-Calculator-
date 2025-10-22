import math

def calc_sine(x):
    x3 = x**3
    x5 = x**5
    x7 = x**7
    x9 = x**9
    x11 = x**11

    return float(x - (x3 / 6.0) + (x5 / 120.0) - (x7 / 5040.0)
                + (x9 / 362880.0) - (x11 / 39916800.0))


def calc_cosine(x):
    x2 = x**2
    x4 = x**4
    x6 = x**6
    x8 = x**8
    x10 = x**10

    return float(1 - (x2 / 2.0) + (x4 / 24.0) - (x6 / 720.0)
                + (x8 / 40320.0) - (x10 / 3628800.0))

def calculate_sin(degrees):
    x_double = math.radians(degrees)

    x_double = x_double % (2 * math.pi)
    if x_double < 0:
        x_double += 2 * math.pi
    x = float(x_double)

    k = int(math.floor(x * 2.0 / math.pi))
    y = float(x - k * math.pi * 0.5)
    quad = int(k % 4)

    match quad:
        case 0:
            return calc_sine(y)
        case 1:
            return calc_cosine(y)
        case 2:
            return -calc_sine(y)
        case 3:
            return -calc_cosine(y)
        case _:
            return 0