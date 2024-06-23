# loop
# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400

list_1 = [100, 200, 300, 400]

for i in range(len(list_1)):
    print(i, list_1[i])