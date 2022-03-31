# 64 bytes
from pickle import NONE

FLAG = b'LINECTF{'


def xor(a: bytes, b: bytes) -> bytes:
    return bytes(i ^ j for i, j in zip(a, b))


S = [None]*4
S[0] = FLAG[0:8]

share1 = [None]*4
str = b""
with open('./Share1', 'rb') as f:
    str = f.read()
    share1[0] = str[0:8]
    share1[1] = str[8:16]
    share1[2] = str[16:24]
    share1[3] = str[24:32]
    f.close()

share4 = [None]*4
with open('./Share4', 'rb') as f:
    str = f.read()
    share4[0] = str[0:8]
    share4[1] = str[8:16]
    share4[2] = str[16:24]
    share4[3] = str[24:32]
    f.close()
print(share4)


flag = [NONE]*8
flag[0] = S[0]
flag[3] = xor(xor(share1[0], share4[0]), S[0])
flag[1] = xor(xor(share1[2], share4[2]), flag[3])
flag[2] = xor(xor(share1[3], share4[3]), S[0])
flag[4] = xor(share4[0], flag[3])
flag[5] = xor(share4[1], flag[2])
flag[6] = xor(share4[2], flag[1])
flag[7] = xor(share4[3], flag[0])

print(flag)
# LINECTF{Yeah_known_plaintext_is_important_in_xor_based_puzzle!!}
