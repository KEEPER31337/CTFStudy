v8 = ""
v7 = "*9J<qiEUoEkU]EjUc;U]EEZU`EEXU^7fFoU^7Y*_D]s" #43글자
v6 = 0;
v4 = 0;
tempstr = ''
tempstr += 'a'*512+v7
print(tempstr)
v8 = tempstr

tempstr = ""
tempstr2 = ""
origlen = 0
for i in range(len(v7)):
    if(v8[i+512] == chr(42)): #*
        tempstr += chr(65) #A
    else: tempstr += v8[i+512];
    tempstr2 += chr(ord(v8[i + 512]) +10);

#A9J<qiEUoEkU]EjUc;U]EEZU`EEXU^7fFoU^7YA_D]s

print(tempstr2)