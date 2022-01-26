from Cryptodome.Cipher import Blowfish
from pwn import *
import base64

# Get keys(K1, K2) by using example 1 and these keys are used to decrypt password
flag = "m6US+8OA+WK1Dl2kLc60Kxp2o3ydWPuXbZK2vBOrQEPTSzH6Od6Qn137Ctn7oLqm7Nb2uvb2wHU="
test_plain = "QUJDREVGR0g="
test_cipher = "J8LFHyoEuoo="

# Perform Encryption & Decryption 2
flag = base64.b64decode(flag)
test_plain = base64.b64decode(test_plain)
test_cipher = base64.b64decode(test_cipher)

K1_list = []
K2_list = []
C1 = []
D2 = []

# Store C1 (Encryption 3) and D2 (Decryption 3)
for i in range(0xff + 1):
    for j in range(0xff + 1):
        K1 = b'\x9e\x91\x9b\xb3\x3a\xef' + bytes([i]) + bytes([j])
        K2 = bytes([i]) + bytes([j]) + b'\xf6\xea\x6d\x93\x7f\x22'
        enc_bf = Blowfish.new(K1, Blowfish.MODE_ECB)
        dec_bf = Blowfish.new(K2, Blowfish.MODE_ECB)
        C1.append(enc_bf.encrypt(test_plain))
        K1_list.append(K1)
        D2.append(dec_bf.decrypt(test_cipher))
        K2_list.append(K2)

# Find K1, K2 by using MITM ( C1 == D2 )
for i in range(len(C1)):
    if C1[i] in D2:
        K1 = K1_list[i]
        break

for i in range(len(D2)):
    if D2[i] in C1:
        K2 = K2_list[i]
        break
    
# Perform Decryption 3 ~ 5
D2_bf = Blowfish.new(K2, Blowfish.MODE_ECB)
D1_bf = Blowfish.new(K1, Blowfish.MODE_ECB)
flag = D2_bf.decrypt(flag)
flag = D1_bf.decrypt(flag)

print("flag is", flag)