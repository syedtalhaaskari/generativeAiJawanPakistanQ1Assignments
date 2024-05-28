# Write a program to check if year is leap year.
# NOTE: search on google of what leap year is.

year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")