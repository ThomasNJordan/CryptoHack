from pwn import *
import binascii

ciphertext = binascii.unhexlify("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
#decoded = "crypto{" + text + "}"
print("Ciphertext: ")
print(ciphertext)

print("Partial Key:")
partialkey = xor(ciphertext, "crypto{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}") #34 Char Flag, 108628598791095240
print(partialkey) # =myXORke0s^Y\x07ZW\\n-zhqD#hF][B\r^DZx&v\x7f\x06^L,vs}

#Gues partial key so myXORke_y

possiblekey = "myXORkeymyXORkeymyXORkeymyXORkey"
print(xor(ciphertext, possiblekey))
# Oh, it was a repeating key... 

x = 2
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

print(xor(partialkey, ciphertext))

''' # Inefficent bruteforce
print("Starting bruteforce: ")
for i in range(50000000000):
    partialkey = ("crypto{" + str(i) + "}")
    attempted = (xor(partialkey), ciphertext)
    if "myXORkey" in attempted[:4]:
        print(attempted)
'''

'''
# Could we do somthing clever and try and bruteforce the first letter to get c?


# Ciphertext has \x04 in middle where { should be and at the end

for i in range(256):
     f = xor("crypto", i)
     if xor(f, "crypto") == 14:
         print("Key is: " + str(f))


#key = 
y = []
for i in ciphertext:
    x = xor(i, key)
    y.append(x)

print(y)
'''