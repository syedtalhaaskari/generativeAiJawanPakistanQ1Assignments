# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

def return_list(*items):
    return list(items)

a = 4
b = 8
c = 10
d = 12

item_list = return_list(a, b, c, d)

print(item_list)
