# Write a Python program to check if a list is empty or not.

list = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]

is_list_empty = 'List is not empty' if len(list) > 0 else 'List is empty'

print(list)
print(is_list_empty)

list2 = []

is_list_empty = 'List is not empty' if len(list2) > 0 else 'List is empty'

print('\n', list2)
print(is_list_empty)