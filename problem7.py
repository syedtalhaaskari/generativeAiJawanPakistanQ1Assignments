# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

from calendar import monthrange

def calc_days(year, month):
    days = monthrange(year, month)
    return days[1]

def take_input():
    year = int(input("Enter the year (YYYY): "))
    month = int(input("Enter the month (1-12): "))
    return year, month

year, month = take_input()

days = calc_days(year, month)

print(f"The number of days in {year}-{month:02d} is: {days}")