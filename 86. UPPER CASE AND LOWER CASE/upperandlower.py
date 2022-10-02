string=input()
count_lower=0
count_upper=0
for i in string:
    if i==i.upper():
        count_upper +=1
    else:
        count_lower+=1
print(count_upper)
print(count_lower)
