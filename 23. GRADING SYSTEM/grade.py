marks=int(input())
if(marks in range(0,101)):
    if marks==100:
        print("S")
    elif marks in range(90,101):
        print("A")
    elif marks in range(80,91):
        print("B")
    elif marks in range(70, 81):
        print("C")
    elif marks in range(60, 71):
        print("D")
    elif marks in range(50, 61):
        print("E")
    else:
        print("F")
else:
    print("Invalid Input")
