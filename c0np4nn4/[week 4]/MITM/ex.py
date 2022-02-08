from Crypto.Cipher import Blowfish
import base64

ciphertext = "m6US+8OA+WK1Dl2kLc60Kxp2o3ydWPuXbZK2vBOrQEPTSzH6Od6Qn137Ctn7oLqm7Nb2uvb2wHU="
ciphertext = base64.b64decode(ciphertext)

pt = "QUJDREVGR0g="
ct = "J8LFHyoEuoo="

p = base64.b64decode(pt)
c = base64.b64decode(ct)

o_k1 = b'\x9e\x91\x9b\xb3\x3a\xef'
o_k2 = b'\xf6\xea\x6d\x93\x7f\x22'

M1 =[]
M2 =[]

for i in range(0, 256):
    for j in range(0, 256):
        k1 = o_k1
        k1 += bytes([i])
        k1 += bytes([j])
        cipher = Blowfish.new(k1, Blowfish.MODE_ECB)
        M1.append(base64.b64encode(cipher.encrypt(p)))
print("M1 finished")

for i in range(0, 256):
    for j in range(0, 256):
        k2 = o_k2
        k2 = bytes([j]) + k2
        k2 = bytes([i]) + k2
        cipher = Blowfish.new(k2, Blowfish.MODE_ECB)
        M2.append(base64.b64encode(cipher.decrypt(c)))
print("M2 finished")

A = (M1 + M2)
B = list(set(M1 + M2))
o_A = A
o_B = B
A.sort()
B.sort()


count = len(B)

for i in range(len(B)):
    if A[0] == B[0]:
        #print(A[0], B[0])
        del A[0]
        del B[0]
    else:
        break
   
M = A[0]

o_k1 = b'\x9e\x91\x9b\xb3\x3a\xef'
o_k2 = b'\xf6\xea\x6d\x93\x7f\x22'

count = 0


index1 = M1.index(M)
key1 = b''


for i in range(0, 256):
    if index1 < count:
        break
    for j in range(0, 256):
        if index1 == count:
            k11 = o_k1
            k11 += bytes([i])
            k11 += bytes([j])
            key1 = k11
        count += 1


count = 0
            
index2 = M2.index(M)
key2 = b''

for i in range(0, 256):
    if index2 < count:
        break
    for j in range(0, 256):
        if index2 == count:
            k22 = o_k2
            k22 = bytes([j]) + k22
            k22 = bytes([i]) + k22
            key2 = k22
        count += 1

Cipher2 = Blowfish.new(key2, Blowfish.MODE_ECB)
Cipher1 = Blowfish.new(key1, Blowfish.MODE_ECB)


plaintext = Cipher2.decrypt(ciphertext)
plaintext = Cipher1.decrypt(plaintext)

print(plaintext)
