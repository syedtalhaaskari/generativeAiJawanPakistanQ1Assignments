# Create a program that calculates and prints the number of days remaining until a person's next birthday.
# take users birth date as input

from datetime import date

def calculate_next_birthday(birth_month, birth_day):
    current_date = date.today()
    current_birth_date = date(current_date.year, birth_month, birth_day)
    next_birth_date = date(current_date.year + 1, birth_month, birth_day)
    
    return ((current_birth_date if current_birth_date > current_date else next_birth_date) - current_date).days

birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

days_remaining = calculate_next_birthday(birth_month, birth_day)

print(f"You have {days_remaining} days until your next birthday.")