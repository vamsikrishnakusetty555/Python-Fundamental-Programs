a=int(input())
b=int(input())
if (a > b):
    greater = a
else:
    greater = b
def lcm(greater):
    if(greater%a==0 and greater%b==0):
        return greater
    return lcm(greater+1)
print(lcm(greater))
