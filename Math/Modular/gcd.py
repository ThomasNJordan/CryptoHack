from pwn import *
import math

# Test Case:
#a = 12
#b = 8

# 1512
a = 66528
b = 52920

#GCD of two numbers is the same as if the larger number was replaced by the differnce of the smaller number.

#gcd a = ib + remainder -> gcd of b, remainder = gcd of a,b
# i is the largest integer that b can be multiplied by to be less than a, or our quotent

# a = bi + r, and r = a%b, then r = a - bi ... we know the gcd of a mod b is also a common divisor of r and b

#gcd(a, b) = a if b = 0
#else gcd(b, a mod b)

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

print(gcd(a, b))
