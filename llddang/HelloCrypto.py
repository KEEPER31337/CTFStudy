import base64, binascii
from Crypto.Util.strxor import strxor

cipher = "MjAxZTMwMjE1MDMxNTYxYzUyMjAzNjY0MzE3ZDUzNzg1MTQ3MmU1YTRkMjQxYjMwMzU3OTZlMGY3ZjRkNDQyYjMwNGY1MzQ1NTE0NTU1NTc1MzRjNTA0NTUyNTc1NTRj"
cipher = base64.b64decode(cipher)
cipher = binascii.unhexlify(cipher)
lenC = len(cipher)

messageXor = strxor(b"HackCTF{", b"HelloCry")

# key를 구해보자!
key = ""
for i in range(8):
  key += chr((cipher[i] - messageXor[i] - 0xdeadbeef) % 128)
for i in range(lenC - 6, lenC):
  key += chr((cipher[i] - ord(key[i- lenC + 6]) - 0xdeadbeef) % 128)

# xor된 message를 구해보자!
message = ""
for i in range(lenC - 14):
  message += chr((cipher[i] - ord(key[i % len(key)]) - 0xDEADBEEF) % 128)

# xor되기 전의 message(flag)를 구해보자!
strxor_key = "HelloCrypto"
strxor_key = (strxor_key * (int(len(message) / len(strxor_key)) + 1))[:len(message)]
strxor_key = strxor_key.encode('utf-8')
message = message.encode('utf-8')
flag = strxor(message, strxor_key)

print(flag)
