### Mausolee (15 points) ###
import numpy

def solve(v, ex):
    ct = v * (10**ex)
    c0 = 10**-11
    lbd = 0.00012
    time = round(1/lbd*(numpy.log(c0/ct)))

    return 2024 - time


print(solve(0.7999, -11))
