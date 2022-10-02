num=int(input())
for i in range(num):
    for j in range(i):
        print(' ',end="")
    for j in range(i,num-1):
        print('*',end='')
    print('*')
