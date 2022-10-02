import math
n=int(input(""))
factorial=[]
for i in range(0,100):
    x=math.factorial(i)
    factorial.append(x)

if n in factorial:
    print("yes")
else:
    print("no")
