print("Give me a flag : ")

v4 = "08'5[Z'Y:H3?X2K3V)?D2G3?H,N6?G$R(G]"
i=0
j=0

tempst = ''
#여기서 v4=08'5[Z'Y:H3?X2K3V)?D2G3?H,N6?G$R(G]
for j in range(len(v4)):
    temp = ord(v4[j]) + 32;
    tempst += chr(temp)
print(tempst)

v4 = tempst[:]
#여기서 v4 = PXGU{zGyZhS_xRkSvI_dRgS_hLnV_gDrHg}
tempst = ''
for i in range(len(v4)):
    if (-101-ord(v4[i])+256) > 64 and (-101 - ord(v4[i])+256) <= 90:
        tempst += chr(-101-ord(v4[i])+256)
    else:
        if (-37 - ord(v4[i])+256) > 96 and (-37 - ord(v4[i])+256) <= 122:
            tempst += chr(-37 - ord(v4[i])+256)
        else: tempst += v4[i]

print(tempst)
