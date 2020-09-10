from Crypto.Util.number import bytes_to_long, long_to_bytes
import codecs
import base64
import binascii

string = "testing oo ahh"

bigint = hex(bytes_to_long(string.encode()))
print("Encoded:" + bigint)

#decoded = decode(long_to_bytes(bigint.decode('utf-8')), "hex")#.decode('utf-8')
#print(decoded)

longDec = long_to_bytes(int(bigint, 0))
decoded = longDec.decode('utf-8')

print(decoded)