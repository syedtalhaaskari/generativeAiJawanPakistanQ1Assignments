# Find Common Elements Between Two Lists
# Objective: Write a Python program that finds and prints the common elements between two lists.
# Example lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(f"List 1: {list1}")
print(f"List 2: {list2}")

common_elements = [x for x in list1 if x in list2]

print(f"Common elements: {common_elements}")