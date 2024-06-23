# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

names_list = []

while True:
    inp = input('Enter a name (Enter "END" to stop name entry): ')
    if inp == "END":
        break
    names_list.append(inp)
    
for name in names_list:
    print("Name:", name)

print("I am done")
