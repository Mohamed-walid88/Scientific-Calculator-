import Cos, Sin


def calculate_tan(d):
    if Cos.calculate_cos(d) == 0 :
        raise ArithmeticError("invalid input")

    return Sin.calculate_sin(d) / Cos.calculate_cos(d)