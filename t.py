from random import randint


count=8
L=[]
print('start')
n=randint(0,7)
L.append(n)
print(f'{n}----{L}')
while count>0 :
    n =randint(0,7)
    print(n)
    for x in range(0,len(L)):
        if n==L[x]:
            break
        else:
            L.append(n)
    count =count-1
print(L,count) 