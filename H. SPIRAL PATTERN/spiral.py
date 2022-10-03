n=int(input())
size=2*n-1
lst=[[0 for x in range(size)] for j in range(size)]
start=0
end=size-1
while(n!=0):
    for i in range(start,end+1):
        for j in range(start,end+1):
            if i==start or i==end or j==start or j==end:
                lst[i][j]=n
    start+=1
    end-=1
    n-=1
for i in range(len(lst)):
    for j in range(len(lst)):
        print(lst[i][j],end="")
    print()
