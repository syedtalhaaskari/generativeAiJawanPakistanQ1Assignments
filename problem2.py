# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'b', 'g', 'd', 'f', 'h']
common = {}

for val_1 in l1:
    for val_2 in l2:
        if val_1 == val_2:
            if val_1 in common:
                common[val_1] = common[val_1] + 1
            else:
                common[val_1] = 1
        elif val_2 not in common:
                common[val_2] = 1
    if val_1 not in common:
        common[val_1] = 1
   
print(common)