n1=int(input())
n2=int(input())
for i in range(n1+1,n2):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
