_list=[]
for i in range(0,5):
    ele=int(input(""))
    _list.append(ele)
a=_list[0]*350.34
b=_list[1]*230.90
c=_list[2]*190.55
d=_list[3]*125.30
e=_list[4]*180.90
sum=a+b+c+d+e
if sum<=15000:
    print("Yes")
else:
    print('No')
