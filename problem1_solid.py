"""
Part 1: Introduction to the Base Class
Understanding BankAccount:

Task: Create a base class called BankAccount with the following attributes and methods:

Attributes:
balance: The initial amount of money in the account.
name: The name of the account.

Methods:
get_balance: Print the current balance.
deposit: Add a specified amount to the balance.
withdraw: Subtract a specified amount from the balance if sufficient funds are available.
transfer: Transfer a specified amount to another account.

Part 2: Creating Specialized Accounts
Interest Rewards Account (InterestRewardsAcct):

Task: add below functionality
1, This account rewards users by adding a 5% bonus to any amount deposited.

Part 3: Creating Specialized Accounts
Savings Account (SavingsAcct):

Task: add below functionality
1. This account rewards users by adding a 5% bonus to any amount deposited.
2. This account charges a $5 fee for every withdrawal.


# use this link if you are unable to create the assignment even after taking help on the group
# use this link only on the next saturday
Ref: https://www.youtube.com/watch?v=PMFd95RgIwE
###############################################################################

Example Test Code:

# PART 1

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.get_balance() # should display $1000
Sara.get_balance() # should display $2000

Sara.deposit(500) # add 500 in Sara's account
Sara.get_balance() # should display $2500

Dave.withdraw(10000) # it should raise an error saying "Sorry, account 'Dave' only has a balance of $1000"
Dave.withdraw(10)   # should subtract $10 from Dave's account
Dave.get_balance()  # should display $990

Dave.transfer(10000, Sara) # it should raise an error saying "Sorry, account 'Dave' only has a balance of $990"
Dave.transfer(100, Sara)   # should add $100 to Sara's account and remove $100 from Dave's account

Dave.get_balance() # should display $890
Sara.get_balance() # should display $2600


# PART 2
# Every InterestRewardsAcct user always receive 5% reward on adding more money
Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100) # it should add $100 + Reward amount of extra 5% i.e (%100 * 1.05)

Jim.get_balance() # it should display $1105

Jim.transfer(100, Dave) # should add $100 to Dave account and remove $100 from Jim's account

Jim.get_balance() # it should display $1005.00


# PART 3
# Every SavingsAcct user always receive 5% reward on adding more money
# Every SavingsAcct user always get panelty of $5 on reducing the money
Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance() # it should display $1000

Blaze.deposit(100)   # it should add $100 + Reward amount of extra 5% i.e (%100 * 1.05)
Blaze.get_balance()  # should display $1105 (instead of 1100)

Blaze.withdraw(10)   # should subtract $15 (instead of $10) from Blaze's account
Blaze.get_balance()  # should display $1090 (instead of 1095)

Blaze.transfer(10000, Sara) # it should raise an error saying "Sorry, account 'Blaze' only has a balance of $1090"
Blaze.transfer(1000, Sara) # it should add $1000 to Sara's account and subtract $1005 from Blaze account (instead of $1000)
Blaze.get_balance()  # should display $85
"""

from abc import ABC, abstractmethod
    
class BalanceErrorException(Exception):
    pass
    
class BankModel(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def transfer(self, amount, target_account):
        pass

class BankAccount(BankModel):
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
    
    def get_balance(self):
        print(f'Name: {self.name}\nCurrent Balance: ${self.balance}')
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Successfully deposit")
        return self.balance
    
    def check_balance(self, amount):
        if amount <= self.balance:
            return
        else:
            raise BalanceErrorException(f"Sorry, account '{self.name}' only has a balance of ${self.balance}")
    
    def withdraw(self, amount):
        try: 
            self.check_balance(amount)
            self.balance -= amount
            print(f"Successfully Withdraw from account")
            return True
        except BalanceErrorException as err:
            print(err)
            return False
    
    def transfer(self, amount, target_account):
        try: 
            if self.withdraw(amount):
                target_account.deposit(amount)
                print(f"Successfully transferred ${amount} from account '{self.name}' to account '{target_account.name}'")
                return True
        except BalanceErrorException as err:
            print(err)
            return False
        
class BonusAccounts(BankAccount):
    bonus = 1.05

    def deposit(self, amount):
        return super().deposit(amount * InterestRewardsAcct.bonus)
        
class InterestRewardsAcct(BonusAccounts):
    pass

class SavingsAcct(BonusAccounts):
    fee = 5

    def withdraw(self, amount):
        return super().withdraw(amount + SavingsAcct.fee)
    
# PART 1
print("PART 1")
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.get_balance() # should display $1000
Sara.get_balance() # should display $2000

Sara.deposit(500) # add 500 in Sara's account
Sara.get_balance() # should display $2500

Dave.withdraw(10000) # it should raise an error saying "Sorry, account 'Dave' only has a balance of $1000"
Dave.withdraw(10)   # should subtract $10 from Dave's account
Dave.get_balance()  # should display $990

Dave.transfer(10000, Sara) # it should raise an error saying "Sorry, account 'Dave' only has a balance of $990"
Dave.transfer(100, Sara)   # should add $100 to Sara's account and remove $100 from Dave's account

Dave.get_balance() # should display $890
Sara.get_balance() # should display $2600

# PART 2
print("\nPART 2")
Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100) # it should add $100 + Reward amount of extra 5% i.e (%100 * 1.05)

Jim.get_balance() # it should display $1105

Jim.transfer(100, Dave) # should add $100 to Dave account and remove $100 from Jim's account

Jim.get_balance() # it should display $1005.00

# PART 3
print("\nPART 3")
Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance() # it should display $1000

Blaze.deposit(100)   # it should add $100 + Reward amount of extra 5% i.e (%100 * 1.05)
Blaze.get_balance()  # should display $1105 (instead of 1100)

Blaze.withdraw(10)   # should subtract $15 (instead of $10) from Blaze's account
Blaze.get_balance()  # should display $1090 (instead of 1095)

Blaze.transfer(10000, Sara) # it should raise an error saying "Sorry, account 'Blaze' only has a balance of $1090"
Blaze.transfer(1000, Sara) # it should add $1000 to Sara's account and subtract $1005 from Blaze account (instead of $1000)
Blaze.get_balance()  # should display $85