speed=float(input())
distance=float(input())
traffic_light_time=float(input())
required_speed=(distance*traffic_light_time)
if (speed>required_speed):
    print("Yes")
else:
    print("No")
