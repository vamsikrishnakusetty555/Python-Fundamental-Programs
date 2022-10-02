string=input()
alpha=0
digits=0
for i in string:
    if i.isalpha()==True:
        alpha+=1
    else:
        digits+=1
print('Characters=',alpha)
print('digits=',digits)


