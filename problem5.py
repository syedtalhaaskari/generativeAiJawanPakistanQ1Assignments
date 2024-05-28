# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100

marks = int(input("Enter marks of subject A out of 100: "))

if marks <= 100 and marks >= 80:
    print("A+")
elif marks < 80 and marks >= 70:
    print("A")
elif marks < 70 and marks >= 60:
    print("B")
elif marks < 60 and marks >= 50:
    print("C")
elif marks < 50 and marks >= 40:
    print("D")
elif marks < 40 and marks >= 33:
    print("E")
elif marks < 33 and marks >= 0:
    print("F")
else: 
    print("Invalid marks")