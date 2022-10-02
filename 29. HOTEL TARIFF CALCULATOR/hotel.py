month=int(input())
rent=float(input())
days=int(input())
if(month>12):
    print("Invalid Input")
else:
    if(month==4 or month==6 or month==11 or month==12):
        rent=rent+(rent*(20/100))
        amount=float(rent*days)
        print('Hotel Tariff: Rs.%.2f'%amount)
    else:
        amount = float(rent * days)
        print('Hotel Tariff: Rs.%.2f' % amount)
