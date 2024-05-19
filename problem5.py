# problem 5
"""
Write a program that:

Asks the user to enter their full name.
Converts the full name to uppercase and prints it.
Asks the user for their favorite number.
Multiplies the number by 2, converts it to a string, and concatenates it to a message.

Prints the message "Your favorite number multiplied by 2 is X.", where X is the new number.
"""

print("\nProblem 5\n")

full_name = input('Enter your full name: ')

upper_case = full_name.upper()

print("\nUppercase:", upper_case)

favorite_number = int(input('\nEnter your favorite number: '))

after_multiply = favorite_number * 2

msg = f"Your favorite number multiplied by 2 is {after_multiply}."

print(msg)
