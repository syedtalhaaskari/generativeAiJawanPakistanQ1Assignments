# problem 4
"""
Write a program that:
Asks the user to enter their age.
Adds 10 to their age.

Prints a message saying "In 10 years, you will be X years old." where X is the new age.
"""

print("\nProblem 4\n")

age = input('Enter your age: ')

after_addition = int(age) + 10

msg = f"\nIn 10 years, you will be {after_addition} years old."

print(msg)
