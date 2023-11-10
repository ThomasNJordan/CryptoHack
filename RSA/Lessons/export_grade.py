# choose the weakest algorithm DH64 by sending Bob only one option from array of Alice's choices

alice = {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x21110c184df62cb7"}
bob = {"B": "0xd52e3cb97f770d30"}

# from alice
ct = {"iv": "befba46eaf17076d4c0e0a81366f0cef", "encrypted_flag": "a5e6bbd8a9f51f894bfbd1f43a219f63f4e042806c1348cdf7c43e5e0ddc9337"}

# A = g^a mod p
# B = g^b mod p

# Calculate inverse of Alice
p = int(alice["p"], 0)
g = int(alice["g"], 0)
A = int(alice["A"], 0)
B = int(bob["B"], 0)

print("A: ", A)
print("B: ", B)
print("p: ", p)
print("g: ", g)

"""
Pohlig-Hellman Algorithm
Using Sagemath:
# Values from MITM attack
A = 8080863703854418428
B = 8898895658504422173
p = 16007670376277647657
g = 2

x = int(pari(f"znlog({int(A)},Mod({int(g)},{int(p)}))"))

# or
x = gp.znlog(A, gp.Mod(g, p))

prin(x)

# x = 2998046103966809316
"""
a = 4071796214858091536

d = pow(B, a, p)

from src.decrypt_08c0fede9185868aba4a6ae21aca0148 import decrypt_flag

shared_secret = d
iv = ct['iv']
ciphertext = ct['encrypted_flag']

print(decrypt_flag(shared_secret, iv, ciphertext))