alpha_values={'A':1,'B':2,'C':3}
x=input("Enter key to check:")
if x in alpha_values.keys():
    print("Key is present and value of the key is:",alpha_values[x])
else:
    print("Key isn't present!")
