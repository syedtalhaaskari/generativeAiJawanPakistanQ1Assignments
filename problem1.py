# Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.

from datetime import date

class Person:
    def __init__(self, name: str, country: str, dob: str):
        self.name = name
        self.country = country
        self.dob = dob
    
    def calc_age(self):
        today = date.today()
        birth_date = date.fromisoformat(self.dob)
        print(int((today.month, today.day) < (birth_date.month, birth_date.day)))
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(age)

talha = Person("Talha", "Pakistan", "1997-08-16")

talha.calc_age()