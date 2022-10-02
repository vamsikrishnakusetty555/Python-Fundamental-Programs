number=int(input())
a=1
b=2
print(a,b+0.0,end=" ")
for i in range(3,number+1):
    if i%2==1:
        a=a*3
        print(a+0.0,end=" ")
    else:
        b=b*3
        print(b+0.0,end=" ")
