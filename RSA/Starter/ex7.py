# Large modulo
N = 510143758735509025530880200653196460532653147
# I used primefac - in src/

import gmpy2
from math import isqrt

def factorize_with_gmpy2(N):
    n = gmpy2.mpz(N)
    factors = []

    # Trial division to remove small factors
    limit = gmpy2.isqrt(n)
    for d in range(2, int(limit) + 1):
        while n % d == 0:
            factors.append(d)
            n //= d

    # If n is not 1, it's a prime factor
    if n > 1:
        factors.append(n)

    return factors

factors = factorize_with_gmpy2(N)
print("Factors:", factors)

'''
from math import ceil, sqrt

# https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
def fermatFactor(N):
    a = ceil(sqrt(N))
    b2 = a * a - N
    while not is_square(b2):
        a += 1
        b2 += 2 * a + 1
    factor1 = a - sqrt(b2)
    factor2 = a + sqrt(b2)
    return factor1, factor2

def is_square(x):
    # Check if x is a perfect square
    return int(sqrt(x) + 0.5) ** 2 == x

print("Beginning Factorization: ")
factor1, factor2 = fermatFactor(N)
print("Factor 1:", factor1)
print("Factor 2:", factor2)
'''