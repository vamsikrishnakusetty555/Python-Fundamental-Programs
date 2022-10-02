size1=int(input())
list1=[]
for i in range(size1):
    ele=int(input())
    list1.append(ele)
size2=int(input())
list2=[]
for i in range(size2):
    ele=int(input())
    list2.append(ele)
list=list1+list2
sort=sorted(list)
print("Sorted List is: ",sort)
'''
list=list1+list2
list_sorted=[]
for i in range(len(list)):
    _min=min(list)
    list_sorted.append(_min)
    list.remove(_min)
print("SORTED : ",list_sorted)'''
