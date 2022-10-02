string=input().split()
str_len=""
length=0
count_words=0
for i in string:
    count_words+=1
    str_len+=i
print(count_words)
if count_words>1:
    length+=len(str_len)+(count_words-1)
    print(length)
else:
    print(len(str_len))
