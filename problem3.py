# problem 3
"""
Problem Statement:

Prompt the user to enter a sentence.
Ask user to replace the word
ask user to replace the word with

Print the modified sentence
"""

print("\nProblem 3\n")

sentence = input('Enter a sentence: ')
word = input('Enter a word to replace: ')
replacing_word = input('Enter a word to replace with: ')

after_replacing = sentence.replace(word, replacing_word)

print("\nOrginal Sentence:", sentence)
print("\nAfter replacing:", after_replacing)
