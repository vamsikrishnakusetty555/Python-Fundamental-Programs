string=input()
index=int(input())
new_str=""
for i in range(len(string)):
    if i==4:
        continue
    else:
        new_str+=string[i]
print(new_str)
