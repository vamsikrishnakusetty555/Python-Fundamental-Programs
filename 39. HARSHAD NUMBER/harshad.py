number=input('')
list=[]
for i in range(0,len(number)):
    list.append(int(number[i]))
sum=sum(list)
if(int(number)%sum)==0:
    print('Harshad Number')
else:
    print("Not Harshad Number")
