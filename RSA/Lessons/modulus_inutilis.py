from src.open_output import open_file
from Cryptodome.Util.number import long_to_bytes

n, e, ct = open_file("src/output_30cff153b7432055fc947fc5abdb57d3.txt")
print("n: ", n)
print("e: ", e)
print("ct: ", ct)

# Because we know the encryption key, we just take the ciphertext to the eth root, finding the original message
# (remember, m^e = ct % n), so it's computationally easy to find the cubed root
from gmpy2 import iroot
pt = iroot(ct, e)[0]
pt = int(pt)

print(long_to_bytes(pt))

# This attack doesn't work with proper padding