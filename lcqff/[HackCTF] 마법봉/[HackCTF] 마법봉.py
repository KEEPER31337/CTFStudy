import hashlib
i = 0

while True:
    if i==10932435112: print(i)

    h = hashlib.sha1()
    h.update(str(i).encode('utf8'))
    res = h.hexdigest()
    if res.startswith("0e") and res[3:].isdigit():
        print(res)
        print(str(i).encode('utf8'))
        break
    else: i+=1
