number=int(input())
rev=0
while number>0:
    last_digit=number%10
    rev=rev*10+last_digit
    number=number//10
print(rev)
