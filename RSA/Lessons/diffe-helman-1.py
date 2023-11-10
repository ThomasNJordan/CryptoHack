p = 991
g = 209
# find d where g * d mod 991 = 1
from src.gcd import extended_gcd
s, t, r = extended_gcd(p, g)
print(s % p, t % p, r % p)

# check for which equals 1
print(g * s % 991)
print(g * t % 991) # this is the correct one

d = t % p
print("d: ", d)

5141855324824926969 + 8003835188138823828