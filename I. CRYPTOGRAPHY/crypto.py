import math
n=int(input())
alpha_ascii=[x for x in range(97,123)]
alpha_char=[]
user_list=[]
for i in range(n):
    ele=input()
    user_list.append(ele)
for i in alpha_ascii:alpha_char.append(chr(i))

#For Mid


for i in user_list:

    first = ""
    last = ""
    mid_char = ""
    temp=i
    if len(temp)%2 !=0:
        mid=len(temp)/2
        mid=math.ceil(mid)
        mid-=1
    else:
        mid = int( len(temp) / 2)
    mid_char=temp[mid]
    for i in range(mid):
            first+=temp[i]

    for i in range(mid+1,len(temp)):
            last+=temp[i]


# For Left Part


    f_len=len(first)
    l_len=len(last)
    f=""
    for i in range(len(first)):
            index=first[i]
            ele = alpha_char.index(index)
            f+=alpha_char[ele-f_len]
            f_len-=1



        #For Right Part
    rev_last=last[::-1]
    last_rev=""
    l=""
    for i in range(len(rev_last)):
            index=rev_last[i]
            ele = alpha_char.index(index)
            l+=alpha_char[ele-l_len]
            l_len-=1
    print(f+mid_char+l[::-1])

