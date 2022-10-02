#PATTERN 5
num=int(input())
for i in range(num):
    for j in range(i,num):
        print(' ',end="")
    for j in range(i):
        print('*',end='')
    print('*')
