import json
import requests
from binascii import unhexlify

res = requests.get(f'http://aes.cryptohack.org/symmetry/encrypt_flag/')

ciphertext = json.loads(res.content)['ciphertext']

iv = ciphertext[:32]
ciphertext = ciphertext[32:]

res = requests.get(f'http://aes.cryptohack.org/symmetry/encrypt/{ciphertext}/{iv}/')

print(unhexlify(json.loads(res.content)['ciphertext']))