size=int(input())
list=[]
for i in range(size):
    ele=int(input())
    list.append(ele)
temp=list[0]
list[0]=list[-1]
list[-1]=temp
'''list[0]=list[0]+list[-1]
list[-1]=list[0]-list[-1]
list[0]=list[0]-list[-1]'''
print(list)

print(list)
