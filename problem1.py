# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".

from datetime import date

def print_current_date():
    current_date = date.today().strftime("%Y-%m-%d")
    print(current_date)

print_current_date()