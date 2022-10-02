row=int(input())
col=int(input())
m1=[]
m2=[]
m3=[]
for i in range(1,col+1):
    m1.append(i)
for i in range(0,row):
    ele=col*i+1
    m2.append(ele)
for i in range(0,row*col+1,col):
    m3.append(i)
m3.remove(0)
tree_no=int(input())
if tree_no in m1:
    print("Yes")
elif tree_no in m2:
    print("Yes")
elif tree_no in m3:
    print("Yes")
else:
    print("No")
