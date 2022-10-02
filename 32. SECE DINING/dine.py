string=input("")
rail=int(input())
string=string.lower()
if string=="front":
    if rail==1:
        print("Left handed")
    elif rail==2:
        print("Right handed")
    else:
        print("Invalid Input")
elif string=="rear":
    if rail==1:
        print("Right handed")
    elif rail==2:
        print("Left handed")
    else:
        print("Invalid Input")
else:
    print("Invald Input")
