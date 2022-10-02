tuple=(4, 6, 2, 8, 3, 1)
print(tuple)
tuple=tuple+(9,)
print(tuple)
tuple=tuple[:5]+(15,20,25)+tuple[:5]
print(tuple)
tuple=list(tuple)
tuple.append(30)
print(tuple)
