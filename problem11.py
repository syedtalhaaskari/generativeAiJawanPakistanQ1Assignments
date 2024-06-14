# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint: 
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

list = [3, 5, 2, 1, 4]

sum = 0

for x in list:
    sum += x
    
print(list)
print(sum)