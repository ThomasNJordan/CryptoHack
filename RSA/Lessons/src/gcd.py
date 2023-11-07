'''
 === Euclid's GCD Algorithm === 
There are three different version of the algorithm to choose from:
1. Division, Modulo Based
2. Subtraction Based (Euclid's Original)
3. Recursive, Modulo Based
https://en.wikipedia.org/wiki/Euclidean_algorithm
'''
def div_gcd(a, b):
    while (b != 0):
        t = b # t is a temp value
        b = a % b
        a = t
    return a

# b = a % b is replaced by repeated subtraction
def sub_gcd(a, b):
    while (a != b):
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# based on the stopping condtion gcd(r_N-1, 0) = r_N-1
def rec_gcd(a, b):
    if b == 0:
        return a
    else:
        return rec_gcd(b, a % b)
    
'''
=== Euclid's Extended Algorithm ===
In addition to the Greatest Common Divisor, this
algorithm also computes the coefficents to Bézout's identity:
ax + by = gcd(a, b); x,y \in \mathbb{R}

In Euclid's Algorithm we can ignore the quotient, here it
is quite important. 

I'm going to use parallel assignments, where (x,y) = (a,b)
means x = a, and y = b
https://kracekumar.com/post/45502206532/python-parallel-assignment/
'''

def extended_gcd(a, b):
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)

    while (r != 0):
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)

    return(old_s, old_t, old_r)
