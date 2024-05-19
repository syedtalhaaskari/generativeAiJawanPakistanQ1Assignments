# problem 7
"""
Problem: Ask the user to input two numbers. 
Calculate their average 
and print the average rounded to 2 decimal places.

NOTE: Concepts Covered: round(), input(), print(), type casting
"""

print("\nProblem 7\n")

num1 = float(input('Enter your first number: '))
num2 = float(input('Enter your second number: '))

average_rounded = round((num1 + num2) / 2, 2)

print(f"\nAverage Rounded: {average_rounded}")
