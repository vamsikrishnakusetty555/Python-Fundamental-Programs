x1=int(input())
y1=int(input())
r1=int(input())
x2=int(input())
y2=int(input())
r2=int(input())
x=((x2-x1)**2+(y2-y1)**2)
import math
distance=math.sqrt(x)

if distance==(r1+r2):
    print("The circles are tangential")
elif distance<(r1+r2):
    print("The circles overlap")
elif distance>(r1+r2):
    print("The circles do not overlap")
