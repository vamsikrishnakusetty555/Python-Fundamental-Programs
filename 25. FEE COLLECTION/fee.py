type=input("Enter the student type\n")
type=type.lower()
def type1():
    t=float(input("Enter tuition fee\n"))
    b=float(input("Enter bus fee\n"))
    cash=float(t+b)
    print("The fees to be paid by the student is Rs.%.2f"%cash)
def type2():
    t = float(input("Enter tuition fee\n"))
    h = float(input("Enter hostel fee\n"))
    cash = float(t + h)
    print("The fees to be paid by the student is Rs.%.2f" % cash)

def type3():
    t = float(input("Enter tuition fee\n"))
    b = float(input("Enter bus fee\n"))
    cash = float((150/100)*t+b)
    print("The fees to be paid by the student is Rs.%.2f" % cash)
def type4():
    t = float(input("Enter tuition fee\n"))
    h = float(input("Enter hostel fee\n"))
    cash = float((150/100)*t + h)
    print("The fees to be paid by the student is Rs.%.2f" % cash)
if (type=="msds"):
    type1()

elif type=="msh":
    type2()
elif type=="mgsds":
    type3()
elif type=="mgsh":
    type4()
else:
    print("Invalid Type")
