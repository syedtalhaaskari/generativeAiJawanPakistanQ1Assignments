# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

nums = []

for i in range(3):
    nums.append(int(input(f"Enter number {i + 1}: ")))
    
nums.sort()

print(nums[1])