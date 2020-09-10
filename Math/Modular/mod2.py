p = 17

print((3 ** 17 )% 17)
print((5 * 17) % 17)
print((7 ** 16) % 17)

#Fermat's little theorem states that if p is a prime number, then a^p-a is a multiple of p. 

p = 65537 # prime
# differnce = 1, therefore answer = 1
print(273246787654 ** 65536 % p)