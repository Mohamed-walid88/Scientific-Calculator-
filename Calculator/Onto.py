import nCr

def calculate_onto(m, n):
    solution = float(0)
    for k in range(n + 1):
        temp = (-1) ** k
        c = float(nCr.calculate_ncr(n, k))
        temp2 = float((n - k) ** m)
        solution += c * temp2 * float(temp)
    return solution
