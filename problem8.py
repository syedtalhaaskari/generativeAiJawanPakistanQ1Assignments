# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.

from datetime import date, timedelta

def calc_date(start_date, days):
    future_date = start_date + timedelta(days=days)
    return future_date

def take_input():
    start_date = date.fromisoformat(input("Enter starting date (YYYY-MM-DD): "))
    days = int(input("Enter number of days to add: "))
    return start_date, days

start_date, days = take_input()

future_date = calc_date(start_date, days)

print(f"The future date is: {future_date}")