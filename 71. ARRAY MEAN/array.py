size=int(input())
list=[]
for i in range(size):
    ele=int(input())
    list.append(ele)
sum=sum(list)
mean=sum/size
print("%.1f"%mean)
