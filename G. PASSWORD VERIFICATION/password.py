password=input().split(",")
for_upper=[i for i in range(65,91)]
for_lower=[i for i in range(97,123)]
alpha_upper=[]
alpha_lower=[]
symbols=['@','#','$']
check=''
count=0
result=[]
for i in for_upper:alpha_upper+=chr(i)
for i in for_lower:alpha_lower+=chr(i)

for i in password:
    if len(i) in range(6,13):
        check=i
        check_upper = [x.isupper() for x in check if x.isalpha() == True]
        check_lower = [x.islower() for x in check if x.islower() == True]
        check_digits = [x.isdigit() for x in check]
        check_symbols = [bool(x) for x in check if x in symbols]
        if any(check_symbols)==True and any(check_lower)==True and any(check_upper)==True and any(check_digits)==True:
            count+=1
            result.append(check)

if count>=1:
    for i in range(len(result)):
        if i==len(result)-1:
            print(result[i])
            break
        print(result[i],end=",")
else:
    print("No password matches the condition")




