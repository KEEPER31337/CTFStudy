#while ( v4[v9] ):
#    v4[v9++] += 2;
#의 결과로 나온 v4 = "ZRIU]HdANdJAGDIAxIAvDDsAyDDq_"
#원래 v4
v9 = 0
v4 = "ZRIU]HdANdJAGDIAxIAvDDsAyDDq_"
orgv4 = ""
while v9 < len(v4):
    orgv4 += chr(ord(v4[v9]) - 2);
    v9 += 1
print(orgv4)
#orgv4 = XPGS[Fb?LbH?EBG?vG?tBBq?wBBo]

temp = "ZRIU]HdANdJAGDIAxIAvDDsAyDDq_"
v10 = 0

v4 = "XPGS[Fb?LbH?EBG?vG?tBBq?wBBo]"
orgv5 = ""
for i in range(len(temp)):
    if(ord(v4[i]) - 13 > 64 and ord(v4[i]) - 13 <= 77):
        orgv5 += chr(ord(v4[v10]) - 13)
    elif ( ord(v4[i]) - 13 > 96 and ord(v4[i]) - 13 <= 109 ):
        orgv5 += chr(ord(v4[i]) - 13);
    elif ord(v4[i]) + 13 > 77 and ord(v4[i]) + 13 <= 90 :
        orgv5 += chr(ord(v4[i]) + 13)
    elif ord(v4[i]) + 13 > 109 and ord(v4[i]) + 13 <= 122:
        orgv5 += chr(ord(v4[i]) + 13);
    else: orgv5 += chr(ord(v4[i]) + 32)


print(orgv5)
#KKTK{So_YoU_ROT_iT_gOOd_jOOb} 근데 이제 앞을 KCTF로 바꿔줘야하는