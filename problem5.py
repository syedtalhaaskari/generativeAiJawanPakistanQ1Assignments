# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

num_list = []
i = 0
max_inp = 5

while i < max_inp:
    inp = int(input('Enter a number: '))
    
    num_list.append(inp)
    i += 1
    
print(f"\nYour inputs: {num_list}")

print(f"\nAverage: {sum(num_list)//max_inp}")
