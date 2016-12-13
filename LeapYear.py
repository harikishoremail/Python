#!usr/bin/python
year = int(input("\nEnter Year to find Leap Year or not: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(year, "is Leap Year.")
else:
    print(year, "is not Leap Year.")
