# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

list = [3, 5, 2, 1, 4]

largest_num = 0

for x in list:
    if x > largest_num:
        largest_num = x
    
print(list)
print(largest_num)