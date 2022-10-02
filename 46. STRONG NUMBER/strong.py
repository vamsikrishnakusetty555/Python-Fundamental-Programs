import math
number=int(input())
fact_sum=0
chk=number
while (number>0):
    last_digit=number%10
    fact_sum=fact_sum+(math.factorial(last_digit))
    number=number//10
if fact_sum == chk:
    print("Strong Number")
else:
    print('Not a Strong Number')
