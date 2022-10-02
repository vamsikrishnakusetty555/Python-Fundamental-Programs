'''
#METHOD 1:
# Without Using Sorted()
list_sorted=[]
for i in range(len(list)):
    _min=min(list)
    list_sorted.append(_min)
    list.remove(_min)
print("SORTED : ",list_sorted)
print(list_sorted[-2])'''

size=int(input())
list=[]
for i in range(size):
    ele=int(input())
    list.append(ele)
sort=sorted(list)
print(sort[-2])
