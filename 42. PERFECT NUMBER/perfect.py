number=int(input())
divisor_sum=0
for i in range(1,number):
    if number%i==0:
        divisor_sum+=i
if divisor_sum==number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
