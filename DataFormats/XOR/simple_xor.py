string = "label"
integer = 13
binary = []

def splitAt(w,n):
    for i in range(0,len(w),n):
        yield w[i:i+n]

#string_byte = 'label'.encode('utf-8')
string_byte = ' '.join(format(ord(x), 'b') for x in string)
print("String to be XOR'd: " + string_byte)
string_binary_string = string_byte.replace(" ", "")
string_binary = int(string_binary_string)

int_byte = "{0:b}".format(integer)
print("Integer to be XOR'd: " + int_byte)
int_binary = int(int_byte)

for s in list(string):
    binary.append(bin(ord(s) ^ 13).lstrip('0b'))

convert = "".join(chr(int(s, 2)) for s in  binary)
print(f'crypto{{{convert}}}')

#result = chr(split_xor)
#print(str(result)) 

