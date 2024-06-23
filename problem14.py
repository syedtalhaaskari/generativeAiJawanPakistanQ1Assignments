# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

def is_divisable_by_11(num):
    return num % 11 == 0

num = 100
print(f"Number: {num} is{'' if is_divisable_by_11(num) else ' not'} divisible by 11")

num = 110
print(f"Number: {num} is{'' if is_divisable_by_11(num) else ' not'} divisible by 11")

num = 231
print(f"Number: {num} is{'' if is_divisable_by_11(num) else ' not'} divisible by 11")

num = 550
print(f"Number: {num} is{'' if is_divisable_by_11(num) else ' not'} divisible by 11")
