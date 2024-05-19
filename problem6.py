# problem 6
"""
Problem: Create a small program that asks the user for their first name and last name, 
converts them to uppercase, 
replaces spaces with hyphens
and calculates the length of their full name.

print 3 variables i.e
print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))

NOTE: Concepts Covered: input(), string methods (upper, replace), len(), print()
"""

print("\nProblem 6\n")

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

full_name = first_name + ' ' + last_name
full_name_upper = full_name.upper()

after_replace = full_name.replace(' ', '_')
full_name_length = len(full_name)

print("\nYour full name in uppercase is:", full_name_upper)
print("Modified sentence:", after_replace)
print("The length of your full name is:", str(full_name_length))