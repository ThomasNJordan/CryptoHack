g = 2

intercepted = {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0xbace546ff8a08befa97da9c9dafe953b8cdf713329867dd2ac557014e2449c910565c79ed6bb53ac7934ea937e5004a410e1d69d8a9cc86c278e1016c2fbe31c81d12b146ae187bdfe58d7cf4edf8b70cd2bcff3387c7e81894acd9386a5afe6687104067365588ccd0fd75cb209bfe6d8c3c2818885423af354ea22ab1ab633b51e55403cdfa3e420127da001c587f7f43b113b88e3b6672169488bddf4ee39c0543edde427f0c11b1d322f20046e997bb67c894f201957c44b261fea569539"}
p = int(intercepted["p"], 0) #, 0 -> lets python detect base
g = int(intercepted["g"], 0)
A = int(intercepted["A"], 0)

import json
fake_a = hex(0)
print("Alice: ", json.dumps({"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": fake_a}))

fake_b = hex(1)
intercepted_bob = {"B": "0x5fe4599f5ace8e3a146ff1c7e2e4db0836a1102f730129cd72c6adcce5ca57a4489f0f7e8e4ec494a7afbbb62b4b247793bc9acd19ffaff0b6ec18202ea6e67729ceb0356f25dabe1370c190df52d420bf3b451586c68385156dc00bd9a00dd5d87a78f40212f4f157321e43bce37fce7cbda724ea1b18f6e0222d238609e5b0c948f287cbd3db72489beb1f1dc84de57342a1f7f188ea955ddb0212a973ea8baaee7886d2d4a0d23de711ecafa022caa0d53dc46c4bdb8b6968f61346ff6df2"}
print("Bob", json.dumps({"B": fake_b}))

# After we send A, bob sends B,

# After we send B, Alice sends back ct

ct = {"iv": "a9709fe2295a58fc068b5741d9148b2d", "encrypted_flag": "169f135c090871b5c110532663a67b1a0b9eead019a41b8461de676f892e88f0"}
s = pow(A, 0, p) # since 0 is fake private key of Alice

from src.decrypt_08c0fede9185868aba4a6ae21aca0148 import decrypt_flag
shared_secret = s
iv = ct['iv']
ciphertext = ct['encrypted_flag']

print(decrypt_flag(shared_secret, iv, ciphertext))