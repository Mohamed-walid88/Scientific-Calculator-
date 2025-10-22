import math,Sin


def calculate_cos(d):
    ans = math.sqrt((1 - (Sin.calculate_sin(d)**2)))

    if ans - 0.1 < 0:
        return 0

    return ans