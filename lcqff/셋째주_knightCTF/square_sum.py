j=0
for i in range(160):
    for j in range(i,160):
        if pow(i,2) + pow(j,2) == 25000:
            print('i=',i,'j=',j)


