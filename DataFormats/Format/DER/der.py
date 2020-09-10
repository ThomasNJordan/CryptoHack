from Crypto.PublicKey import RSA
import OpenSSL.crypto

data = open('2048b-rsa-example-cert.der', 'rb').read()
print(RSA.importKey(OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_ASN1, OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, data).get_pubkey())).n)