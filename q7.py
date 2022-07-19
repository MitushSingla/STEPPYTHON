print("Leap year in python:")
year=2004
if (year % 400 == 0) and (year % 100 ==0):
    print(year,"is a leap year")
else:
    print(year,"is not leap year")