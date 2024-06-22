"""
Create a dictionary named employee_data with the following key-value pairs:
"John": 55000
"Emma": 60000
"Harry": 70000
"Sophia": 65000
"Mike": 48000

1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names.
2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly.
"""

print("Problem No. 2")

employee_data = {
    "John": 55000,
    "Emma": 60000,
    "Harry": 70000,
    "Sophia": 65000,
    "Mike": 48000,
}

print("\Employee Dictionary:", employee_data)

print("\nBefore Salary Increase:")

for name, salary in employee_data.items():
    if salary > 60000:
        print(f"Employee Name: {name}, Salary: {salary}")
    employee_data[name] = int(employee_data[name] * 1.1)

print("\nAfter Salary Increase:")

for name, salary in employee_data.items():
    print(f"Employee Name: {name}, Salary: {salary}")
