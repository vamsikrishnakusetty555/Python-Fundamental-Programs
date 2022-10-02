d1={'A':1,'B':2}
d2={'C':3}
print("Concatenated dictionary is:")
l_keys=list(d2.keys())
l_values=list(d2.values())
for i in range(len(d2)):
    d1[l_keys[i]]=l_values[i]
print(d1)
'''
print({**d1,**d2})
d1.update(d2)
print(d1)
result=d1|d2
print(result)'''
