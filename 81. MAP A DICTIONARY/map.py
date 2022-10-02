n=int(input("Enter number of elements for dictionary:"))
d={}
keys=[]
values=[]
print("For keys: ")
for i in range(n):
    ele=input()
    keys.append(ele)
print("For values: ")
for i in range(n):
    ele=input()
    values.append(ele)
print("The dictionary is: ")
for i in range(n):
    d.update({keys[i]:values[i]})
    '''d[keys[i]]=values[i]'''
print(d)
'''for i in range(1,n+1):
    keys=input("Enter key: ")
    values=input("Enter Value: ")
    d.update({keys:values})'''
