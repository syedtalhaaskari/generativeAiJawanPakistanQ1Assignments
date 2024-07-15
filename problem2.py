# Write a Python program to create a calculator class.
# Include methods for basic arithmetic operations

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")

    def subtract(self):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")

    def multiply(self):
        print(f"{self.num1} * {self.num2} = {self.num1 * self.num2}")

    def divide(self):
        print(f"{self.num1} / {self.num2} = {self.num1 / self.num2}")

    def remainder(self):
        print(f"{self.num1} % {self.num2} = {self.num1 % self.num2}")

col1 = Calculator(6, 3)
col1.add()
col1.subtract()
col1.multiply()
col1.divide()
col1.remainder()

print()

col2 = Calculator(5645, 213)
col2.add()
col2.subtract()
col2.multiply()
col2.divide()
col2.remainder()
