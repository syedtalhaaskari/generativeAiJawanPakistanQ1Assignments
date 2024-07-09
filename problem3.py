# Write a program that takes a birth year as input and calculates the age of a person.

from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))

age = calculate_age(birth_year)

print(f"Your current age is {age} years.")