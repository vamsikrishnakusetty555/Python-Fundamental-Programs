n1=int(input())
n2=int(input())
count_n1=0
count_n2=0
for i in range(1,n1+1):
    if n1%i==0:
       count_n1+=i
for i in range(1,n2+1):
    if n2%i==0:
            count_n2+=i
if (count_n1//n1)==(count_n2//n2):
    print("Friendly Pair")
else:
    print('Not Friendly Pair')
