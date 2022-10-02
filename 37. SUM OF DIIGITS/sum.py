n=int(input())
sum=0
while True:
    ld=n%10
    sum=sum+ld
    n=n//10
    if n<=0:
        break
print(sum)
