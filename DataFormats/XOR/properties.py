from bitstring import BitArray

'''
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2 ^ KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2 ^ KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" 
'''

KEY1 = BitArray(hex="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313").bin[2:] # KEY 1
RESULT1 = BitArray(hex="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e").bin[2:] # KEY 2 ^ KEY 1
RESULT2 = BitArray(hex="c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1").bin[2:] # KEY 2 ^ KEY 3
RESULT3 = BitArray(hex="04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf").bin[2:] # FLAG ^ KEY 1 ^ KEY 3 ^ KEY 2

print("################################" * 5 + "\n" + "Givens:" + "\n" + KEY1 + "\n" + RESULT1 + "\n" + RESULT2 + "\n" + RESULT3 + "\n" + "################################" * 5)

KEY2_gibberish = int(KEY1,2) ^ int(RESULT1,2)
KEY2 = '{0:b}'.format(KEY2_gibberish)
print("KEY 2: " + KEY2)

KEY3_gibberish = int(KEY2, 2) ^ int(RESULT2,2)
KEY3 = '{0:b}'.format(KEY3_gibberish)
print("KEY 3: " + KEY3)

FLAG_gibberish = int(RESULT3, 2) ^ int(KEY1, 2) ^ int(KEY2, 2) ^ int(KEY3, 2)
FLAG = '{0:b}'.format(FLAG_gibberish)
print("BINARY FLAG: " + FLAG)

x = ' '.join([str(FLAG)[i:i+7] for i in range(0, len(str(FLAG)), 7)])

print(x)