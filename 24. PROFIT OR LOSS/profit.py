x=float(input())
y=float(input())
print('''Enter the price of a dozen mangoes
Enter the price at which 1 mango is being sold''')
if(y*12==x):
    print("No profit nor loss")
elif(y*12>x):
    profit=float((y*12)-x)
    print("Profit : Rs.%.2f"%profit)
elif(y*12<x):
    loss=float(x-(y*12))
    print("loss : Rs.%.2f"%loss)

