size=int(input())
list=[]
for i in range(size):
    ele=int(input())
    list.append(ele)
non_duplicates=[]
for i in list:
    if i not in non_duplicates:
        non_duplicates.append(i)
print(non_duplicates)
'''
or
convert the list into set
'''
