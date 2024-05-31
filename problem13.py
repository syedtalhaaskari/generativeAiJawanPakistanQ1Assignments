# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

nums = []

for i in range(3):
    nums.append(int(input(f"Enter number {i + 1}: "))) 
        
nums.sort()

second_largest = nums[0]

for i in range(0, 2):
    if (nums[i] < nums[i + 1]): second_largest = nums[i]

print(second_largest)

"""
    1
    Input: 5 10 10
    Output: 10
     
    2
    Input: 5 10 15
    Output: 10
    
    3
    Input: 10 10 10
    Output: 10   
"""