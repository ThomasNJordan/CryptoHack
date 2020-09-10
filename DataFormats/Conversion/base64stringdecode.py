import base64

encoded = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Remember, to convert: Encoded -> ASCII Values -> B64 Bytes -> Bytes -> ASCII

hexbytes = encoded.decode("hex")
#hexbytes = bytearray.fromhex(encoded).decode()

bytes = base64.b64decode(hexbytes)
text = str(bytes, "utf-8")

print(text)
