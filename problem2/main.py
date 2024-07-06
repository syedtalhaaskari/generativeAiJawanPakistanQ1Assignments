# Create a new text file named "student_records.txt" with the following initial content:
# Student ID | Student Name | Grade
# 101       | Alice        | A
# 102       | Bob          | B
# 103       | Carol        | C

# Open the "student_records.txt" file in read mode ('r') and read its contents line by line. Print each line to the console.

# Create a new text file named "updated_records.txt" in write mode('w').
# Read the content of "student_records.txt" again and write only the lines containing students with grades 'A' or 'B' to the "updated_records.txt" file.
# Close both files.

# Open "updated_records.txt" in append mode('a') and add a new student record:
# Close the "updated_records.txt" file.

# Open "updated_records.txt" in read mode and print its contents to the console to verify that the new student record has been added.

f = open('student_records.txt', 'r')

data = f.readline()

while data:
    print(data, end='')
    data = f.readline()

f.seek(0)
wf = open('updated_records.txt', 'w')

print("\n\nAdding student records in updated list who got 'A' and 'B' grade")

data = f.readline()
wf.write(data)

while data:
    ind = data.rfind('| ')
    item = data[ind + 2]
    if item == 'A' or item == 'B':
        wf.write(data)
    data = f.readline()
f.close()
wf.close()

af = open('updated_records.txt', 'a')
af.write('104       | Talha        | A')

af.close()

f = open('updated_records.txt', 'r')

data = f.read()

print("\nAfter writing updated records")
print(data)

f.close()