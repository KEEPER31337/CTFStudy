
ct = "IihsIb_7[^7is<inH][l_^D`Ib_;[n7iu"

ctarr = []
for ch in ct:
    ctarr.append(ord(ch))

print(ctarr)
print(ctarr[-1])
print(chr(117))
print(chr(122))
for i in range(len(ctarr)):
    if 91 <= ctarr[i] <= 116:
        ctarr[i] += 6

    elif 54 <= ctarr[i] <= 79:
        ctarr[i] += 11

code = "".join(chr(c) for c in ctarr)



ct = "6G:653"

ctarr = []
for ch in ct:
    ctarr.append(ord(ch))

for i in range(len(ctarr)):
    if 91 <= ctarr[i] <= 116:
        ctarr[i] += 6

    elif 54 <= ctarr[i] <= 79:
        ctarr[i] += 11


place = "".join(chr(c) for c in ctarr)


print("[+] place : " + place)
print("[+] passwd: " + code)
print("KCTF{" + place + "_" + code + "}")


