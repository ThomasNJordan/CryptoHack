from src.gcd import extended_gcd

p = 857504083339712752489993810777  # primes
q = 1029224947942998075080348647219 # primes
e = 65537 # exponent

N = (p-1)*(q-1) # Totient

# Decryption key is Bézout coefficients' old_s
d = extended_gcd(e, N)
d = d[0] % N # because Bézout coefficients can overflow bounds
print("Decryption Key: ", d)

'''
# You can also use Euler's totient function
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
print(d)
'''