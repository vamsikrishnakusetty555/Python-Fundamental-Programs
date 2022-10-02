number=int(input())
start=95.0
difference=20.5
i=0
while(i<number*2):
    if(i%2==0):
        print(start, end=" ")
        start=start+difference+i
    i+=1
