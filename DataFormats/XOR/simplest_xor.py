msg = ""
for c in "label":
	i = ord(c) ^ 13	
	msg += chr(i)
print(msg)