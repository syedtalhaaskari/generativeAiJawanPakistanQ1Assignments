# Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        print(f"Hello {name} your new bank account has been created successfully with the initial balance of Rs {initial_balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs {amount} into your account. New balance: Rs {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew Rs {amount} from your account. New balance: Rs {self.balance}")
        else:
            print("Insufficient funds")
    
    def display_balance(self):
        print(f"Your current balance is: Rs {self.balance}")
            
my_account = Bank("Talha", 10000)

my_account.deposit(5000)

my_account.withdraw(2000)

my_account.display_balance()
