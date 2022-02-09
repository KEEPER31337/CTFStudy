from Crypto.Cipher import Blowfish
import base64

decode=lambda x:base64.b64decode(x)

pw = "m6US+8OA+WK1Dl2kLc60Kxp2o3ydWPuXbZK2vBOrQEPTSzH6Od6Qn137Ctn7oLqm7Nb2uvb2wHU="
plaintext = "QUJDREVGR0g="
ciphertext = "J8LFHyoEuoo="
#plain을 key1을 통해 암호화한 값 x가 나오고
#그것을 다시 key2를 통해 암호화 시키면 cipher 이 나온다.

K1 = "9e919bb33aef"#뒤에 두개 없음
K2 = "f6ea6d937f22"#앞에 두개 없음
realK1, realK2 = "",""


#K1과 K2의 조각을 찾아야 한다.
def find_piece(K1,K2,plaintext,ciphertext):
    for i in range(0xff +1):
        for j in range(0xff +1):
            text = chr(i).encode()+ chr(j).encode() #byte
            print(blowfish_en(bytes.fromhex(K1+text.hex())), " == ", blowfish_de(bytes.fromhex(text.hex()+K2)))
            if blowfish_en(bytes.fromhex(K1+text.hex())) == blowfish_de(bytes.fromhex(text.hex()+K2)):
                realK1, realK2 = K1+text, text+K2
                print("찾음")
                return
            #온전한 K1을 사용해 암호화한 plaintext와 key2를 사용해 복호화한 ciphertext가 동일해야한다.
            #아니... 같은 게.... 안나오는데........


def blowfish_en(key):
    D = Blowfish.new(key, Blowfish.MODE_ECB)
    x = D.encrypt(decode(plaintext))
    return x
    #Blowfish 알고리즘을 사용해 복호화한다.

def blowfish_de(key):
    D = Blowfish.new(key, Blowfish.MODE_ECB)
    x = D.decrypt(decode(ciphertext))
    return x
    #Blowfish 알고리즘을 사용해 암호화한다.

find_piece(K1,K2,plaintext,ciphertext)
print("real= ",realK1+realK2)