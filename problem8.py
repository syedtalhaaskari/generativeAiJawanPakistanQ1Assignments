# problem 8
"""
Problem: Ask the user to input a sentence. 
Replace all spaces with underscores 
and split the sentence into words.

NOTE: Concepts Covered: replace(), split(), input(), print()
"""

print("\nProblem 8\n")

sentence = input('Enter a sentence: ')

replaced_sentence = sentence.replace(' ', "_")
splitted_sentence = sentence.split(" ")

print(f"\nAfter Replacing: {replaced_sentence}")
print(f"\nAfter Splitting: {splitted_sentence}")
