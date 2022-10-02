number=int(input())
list=[]
def bin(x):
    if x==0:
        return 0
    else:
        digit=x%2
        list.append(digit)
        return bin(x//2)
bin(number)
list.reverse()

for i in list:
    print(i,end="")
