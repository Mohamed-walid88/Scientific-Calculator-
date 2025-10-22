import Cos

def calculate_sec(d):
    if Cos.calculate_cos(d) == 0:
        raise ArithmeticError("invalid input")

    return 1 / Cos.calculate_cos(d)