import math
from codecs import decode

hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
char_hex = bytes.fromhex(hex).decode()

i = 0
key = 1

while i <= 101:
    key = key + 1
    i = i + 1

flag = ""

for byte in hex:
    print("A")

while key <= 256:
    for c in char_hex:
        i = ord(c) ^ key
        flag += chr(i)
    if "crypto" in flag:
        print(flag)