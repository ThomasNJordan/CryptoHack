import math
import binascii

array = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125] 

s = ""

for int in array:   
    decode = chr(int)
    s += decode

print(s)