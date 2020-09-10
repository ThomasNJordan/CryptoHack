import binascii
import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import json

BLOCK_SIZE = 32
#ciphertext = binascii.hexlify(ciphertext)

print('Ciphertext')
data = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/').json()

flag_ciphertext = data['ciphertext']
print(flag_ciphertext)
print(binascii.unhexlify(flag_ciphertext))

flag_enc_bytes = binascii.unhexlify(flag_ciphertext)
enc_decoded = []
for b in flag_enc_bytes:
    enc_decoded.append(chr(b))
print(''.join(enc_decoded))
