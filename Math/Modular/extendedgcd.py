# Primes
p = 26513
q = 32321

# Standard Euclid: 
def gcd(a, b):
    if (a == 0):
        return(b)
    if (b == 0):
        return(a)
    if (a == b):
        return(a)
    if (a > b):
        while b != 0:
            (a , b) = (b, a % b)
        return(a)

gcd = gcd(p, q)

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# Extend -> p * u + q * v = gcd(p,q)
# gcd = p * u + q * v

if gcd == None:
    print(egcd(26513,32321)) # = 10245, -8404
