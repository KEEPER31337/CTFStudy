import math

x = 1
y = 2
answer = 0
t = 1 # xy값 구할때 x에 곱해줄 값

while x!=667:
    if y == math.pow(10,t):
        t+=1
        print('y='+ str(y) +' math.pow(10,t)=' + str(math.pow(10,t)))
        print("x*math.pow(10,t) + y = ",x*math.pow(10,t) + y)
        print('answer='+str(answer))
    answer += (x*y) + x*math.pow(10,t) + y

    x += 1
    #y += 1
print(x)
print(answer)

#왜 설명을 똑바로 안적어두는거임
#y는 +=1하는게 아니었음
