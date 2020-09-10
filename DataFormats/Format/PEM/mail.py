from Crypto.PublicKey import RSA

f = open('keypair.pem', 'r')
Key = RSA.importKey(f.read())
target = Key.d

print(target)