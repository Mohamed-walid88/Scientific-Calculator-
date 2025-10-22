import Sin

def calculate_csc(d):
    if Sin.calculate_sin(d) == 0:
        raise ArithmeticError("invalid input")

    return 1 / Sin.calculate_sin(d)