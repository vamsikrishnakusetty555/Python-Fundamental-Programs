number=int(input())
l=[]
def binary(number):
    if number==0:
        return 1
    else:
        digit=number%2
        l.append(digit)
        binary(number//2)
binary(number)
l.reverse()
for i in l:
    print(i,end="")
