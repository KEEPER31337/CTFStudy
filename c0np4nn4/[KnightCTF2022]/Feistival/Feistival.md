# Description
![image](https://user-images.githubusercontent.com/49471288/150627020-5998e011-38eb-471e-9195-46e01cb7a13e.png)
#### I had no idea of the title but It become clearly after I read the encryptor script.
---

![image](https://user-images.githubusercontent.com/49471288/150627039-78fa2a9c-4cad-4860-ae84-85abf0dbae8a.png)
#### Through the link, There are two files.
#### cipher.txt is not readable txt file. It's just a bunch of byte.
---

# enc.py
```python
m, n = 21, 22
def f(word, key):
    out = ""
    for i in range(len(word)):
        out += chr(ord(word[i]) ^ key)
    return out

flag = open("flag.txt", "r").read()

L, R = flag[0:len(flag)//2], flag[len(flag)//2:]
x = "".join(chr(ord(f(R, m)[i]) ^ ord(L[i])) for i in range(len(L)))
y = f(R, 0)

L, R = y, x
x = "".join(chr(ord(f(R, n)[i]) ^ ord(L[i])) for i in range(len(L)))
y = f(R, 0)

ciphertext = x + y
ct = open("cipher.txt", "w")
ct.write(ciphertext)
ct.close()
```

Description of Encryption process
1. Seperate the flag file into L, R blocks
2. Manipulating each blocks and save them as a new blocks
3. After 2 rounds, concatenate the blocks to make ciphertext

As you can see, It's a simple implement of feistel structure cipher and f function is consist of ONLY xor so it's obviously reversible.

After short doodling, I can easily write the decryptor script.

![image](https://user-images.githubusercontent.com/49471288/150628183-9ecb138b-2685-46f9-bb1b-b03aec868ae0.png)
