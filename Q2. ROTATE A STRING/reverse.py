s=input()
n=int(input())
start=0
lst=[]

for i in s:
    lst.append(i)
    
while True:
    last=lst.pop()
    lst.insert(0,last)
    start+=1
    if(start==n):
        break
for i in lst:
    print(i,end="")
