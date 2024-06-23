# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

l1 = [11, 33, 50]

result = ""

for item in l1:
    result += str(item)
    
print(f"List: {l1}")
print(f"Result: {result}")