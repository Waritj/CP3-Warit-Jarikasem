Speed = float(input("Please iput speed (km/hr): "))
Time = float(input("Please input time (hour): "))
if Speed >= 1 and Time >= 1:
    print(Speed/Time, "km/h")
else: print("Speed and Time must be greater than 1")
