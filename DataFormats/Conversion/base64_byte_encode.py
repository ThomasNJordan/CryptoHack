import base64

hex_encoded = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Remember, to convert: Encoded -> ASCII Values -> B64 Bytes -> Bytes -> ASCII

#hexbytes = bytearray.fromhex(hex_encoded).decode()
#b64_encoded = base64.b64encode(hexbytes)
#print(b64_encoded)

x = bytes.fromhex(hex_encoded)
b64_encoded = base64.b64encode(x)
print(b64_encoded)