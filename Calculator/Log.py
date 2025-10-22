import Ln

def calculate_log(b, a):
    if a == 1:
        return 0
    if a == b:
        return 1

    return Ln.calculate_ln(a) / Ln.calculate_ln(b)