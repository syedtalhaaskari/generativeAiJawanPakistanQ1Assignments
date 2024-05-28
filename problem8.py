# Write a program to ask user its name and check whether name consists of 5 or more letters

name = input("Enter your name: ")

if len(name) >= 5:
    print(f'Your name "{name}" consists of more than 5 letters')
else:
    print(f'Your name "{name}" consists of less than 5 letters')