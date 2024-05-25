# problem 1
"""
Problem Statement:

Prompt the user to enter a float number.
Use the round() function to round the number to 2 decimal places.
Print the original number and the rounded number.
Use the len() function to find the length of a string entered by the user and print the result.
"""

print("\nProblem 1\n")

org_num = input('Enter a number: ')
round_num = round(float(org_num), 2)

print("Orginal Number:", org_num)
print("Rounded Number:", round_num)
print("Num length:", len(org_num))
