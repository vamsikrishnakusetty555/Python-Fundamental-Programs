item=int(input("Enter the number of items\n"))
heating_time=float(input("Enter the single item heating time\n"))
if item<=2:
    rec_time=heating_time+((50/100)*5)
    print("The recommended heating time is %.2f"%rec_time)
elif item==3:
    rec_time=2*(heating_time)
    print("The recommended heating time is %.2f"%rec_time)
elif item>3:
    print("Number of items is more")
