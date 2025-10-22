import Tan

def calculate_cot(d):
    if Tan.calculate_tan(d) == 0:
        raise ArithmeticError("invalid input")

    return 1 / Tan.calculate_tan(d)