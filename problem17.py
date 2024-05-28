"""
Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

If the years of service are less than 5, no bonus.
If the years of service are between 5 and 10, bonus is 10% of the salary.
If the years of service are more than 10, bonus is 20% of the salary.
Print the bonus amount.
"""

salary = int(input("Enter your salary: "))
years = int(input("Enter your years of service: "))

if years < 5 and years > 0:
    print("No bonus.")
elif years >= 5 and years <= 10:
    bonus = salary * 0.1
    print(f"Your bonus is {bonus}")
elif years > 10:
    bonus = salary * 0.2
    print(f"Your bonus is {bonus}")
else:
    print("Invalid Input.")