# problem 2
"""
Problem Statement:

Prompt the user to enter a sentence.
Convert the entire sentence to uppercase.
Convert the entire sentence to lowercase.
Capitalize the first word of the sentence.

Print each of these modified sentences.
"""

print("\nProblem 2\n")

sentence = input('Enter a sentence: ')

upper_case = sentence.upper()
lower_case = sentence.lower() 
third_case = sentence.split(' ')
third_case[0] = third_case[0].upper()
third_case = ' '.join(sentence)

print("\nOrginal Sentence:", sentence)
print("\nUppercase:", upper_case)
print("Lowercase:", lower_case)
print("Titlecase:", third_case)
