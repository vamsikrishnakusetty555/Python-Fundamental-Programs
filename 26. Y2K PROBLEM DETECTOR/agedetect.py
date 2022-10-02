by=input("Enter Year of Birth\n")
cy=input("Enter Current year\n")
if(by>'22'):
    by='19'+by
    by=int(by)

elif(by<='22'):
    by='20'+by
    by=int(by)

if (cy > '22'):
    cy = '19' + cy
    cy = int(cy)

elif (cy <= '22'):
    cy = '20' + cy
    cy = int(cy)
    
age=cy-by
print('Your age is ',age)
