# Write a program to check whether a number is divisible by 7

mark = int(input("Enter a number: "))

if mark % 7 == 0:
    print(f"{mark} is divisible by 7")
else:
    print(f"{mark} is not divisible by 7")