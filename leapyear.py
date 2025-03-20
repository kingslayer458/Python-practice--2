def verify_leap(year):
    if (year%4==0 and year%100 != 0) or (year%400==0):
        return True
    return False

year = int(input("enter the year"))
if verify_leap(year):
    print("leap year")
else:
    print("not a leap year")
