# Write a program to check if year is leap year.
# NOTE: search on google of what leap year is.

year = int(input("Enter a year: "))

msg = ''
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    msg = f"{year} is a leap year"
else:
    msg = f"{year} is not a leap year"

print(msg)