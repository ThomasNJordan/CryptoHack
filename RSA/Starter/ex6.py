from Cryptodome.Util import number
from Cryptodome.Hash import SHA256

privatekey = open("src/private_0a1880d1fffce9403686130a1f932b10.key")
privatekey_data = privatekey.read()

# Extract N and d from the file data
N = int(privatekey_data.split('N = ')[1].split('\n')[0])
d = int(privatekey_data.split('d = ')[1])

# Print the extracted values (optional)
print("N:", N)
print("d:", d)

# Calculate hash of message
h = SHA256.new(data=b'crypto{Immut4ble_m3ssag1ng}')

# .digest() returns the raw binary data of the hash
message_hash = number.bytes_to_long(h.digest())

# Sign the message (S = H(M)^d1 mod N_1)
signature = pow(message_hash, d, N)

# Print the signature
print("Signature:", signature)
