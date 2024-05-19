# problem 1
"""
Problem Statement:

Prompt the user to enter a float number.
Use the round() function to round the number to 2 decimal places.
Print the original number and the rounded number.
Use the len() function to find the length of a string entered by the user and print the result.
"""

print("\nProblem 1\n")

num1 = float(input('Enter a number: '))

print("Orginal Number:", num1)
print("Rounded Number:", round(num1, 2))

msg = input("\nEnter a msg: ")
print("Msg length:", len(msg))
