# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list
# numbers = [12, 7, 9, 24, 18, 5, 3, 20]

numbers = [12, 7, 9, 24, 18, 5, 3, 20]

even_count = 0
odd_count = 0

for x in numbers:
    if x % 2 == 0: 
        even_count +=1 
    else:
        odd_count += 1
    
print(numbers)
print(f"Even Count: %d" % even_count)
print(f"Odd Count: %d" % odd_count)