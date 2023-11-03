# Encrypt the "message"
message = 12 # message
p = 17 # primes
q = 23 # primes
e = 65537 # exponent 
N = p*q

# ciphertext = m^e % N
ciphertext = message ** e % N

print(ciphertext)