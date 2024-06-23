# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

def get_highest(num1, num2):
    return num1 if num1 > num2 else num2

num_1 = 3400
num_2 = 100
print(f"Number 1: {num_1}")
print(f"Number 2: {num_2}")
print(f"Greate Number: {get_highest(num_1, num_2)}")
