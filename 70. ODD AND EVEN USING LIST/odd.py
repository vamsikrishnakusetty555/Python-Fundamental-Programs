size=int(input())
list=[]
even=[]
odd=[]
for i in range(size):
    ele=int(input())
    list.append(ele)
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("The even list ",even)
print("The odd list ",odd)
