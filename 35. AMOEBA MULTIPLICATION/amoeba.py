months=int(input("Enter the number of Months :\n"))
fibo=[0,1]
for i in range(1,12):
        sum=fibo[i]+fibo[i-1]
        fibo.append(sum)
size=fibo[months-1]
print('The amoeba size is ',size)
