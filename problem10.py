# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc

num = 2

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")