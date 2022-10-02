n=int(input())
start=0
i=1
while(i<=n):
    if(i%2==0):
        start=pow(i,2)-2
        print(start,end=" ")
    else:
        start=pow(i,2)-1
        print(start,end=" ")
    i+=1

