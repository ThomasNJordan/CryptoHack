from bitstring import BitArray
from pwn import xor

'''
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
'''

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313") # KEY 1
RESULT1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e") # KEY 2 ^ KEY 1
RESULT2 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1") # KEY 2 ^ KEY 3
RESULT3 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf") # FLAG ^ KEY 1 ^ KEY 3 ^ KEY 2

KEY2 = xor(KEY1, RESULT1)
KEY3 = xor(KEY2, RESULT2)
FLAG = xor(KEY1, KEY2, KEY3, RESULT3)

print(FLAG)