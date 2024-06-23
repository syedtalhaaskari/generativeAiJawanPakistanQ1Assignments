# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”

while True:
    inp = input('Enter something but not "0": ')

    if inp == '0':
        print('I told you not to enter "0" now good bye')
        break
    print('Your input was', inp)
