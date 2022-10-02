number=int(input())
if number>1:
    for i in range(2,number):
        if number%i==0:
            print("Not a Prime")
            break
    else:
        print("Prime Number")

    
'''
number=int(input())
count=0
if number>1:
    for i in range(1,number):
        if number%i==0:
            count+=1
else:
    print("Not a prime")
if count==1:
    print("Prime Number")
else:
    print("Not a prime")'''
