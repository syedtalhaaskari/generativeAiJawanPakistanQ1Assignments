"""
create the same ATM machine program that we do in last class.
features:
    allow only affiliated_card if age < 60
    allow govt employee regardless of age and affiliated_card
    charge 10 Rs more if grade is less than 18

# hint: filename: if_statement/if_with_nested_if.py
"""

balance = 0
my_profit = 10

# Senior Citizen
is_senior_citizen = int(input("Enter your age: "))
if is_senior_citizen >= 18 and is_senior_citizen < 60:
    is_senior_citizen = False
elif is_senior_citizen >= 60:
    is_senior_citizen = True
else:
    print("Invalid age")
    exit()

# Affiliated Card
affiliated_card = True # meezan
affiliated_card = input("Do you have affiliated card(Y/N): ")[0].lower()
if affiliated_card == 'y':
    affiliated_card = True
elif affiliated_card == 'n':
    affiliated_card = False
else:
    print("Invalid Input")
    exit()

# Government Employee
high_grade = False
is_govt_employee = input("Are you Government Employee(Y/N): ")[0].lower()
if is_govt_employee == 'y':
    is_govt_employee = True
    
    # Checking Grade
    high_grade = input("Is your grade more or equal to 18(Y/N): ")[0].lower()
    if high_grade == 'y':
        high_grade = True
    elif high_grade == 'n':
        high_grade = False
    else:
        print("Invalid Input")
        exit()
elif is_govt_employee == 'n':
    is_govt_employee = False
else:
    print("Invalid Input")
    exit()

print("Initital balance", balance)
    
# Deposit Amount
deposit_amount = int(input("Enter the amount to deposit: "))

if deposit_amount < 0:
    print("Invalid Input")
    exit()

balance += deposit_amount

print("After first depost:", balance)

# Credit Amount
withdraw_amount = int(input("Enter the amount to withdraw: "))

if withdraw_amount < 0:
    print("Invalid Input")
    exit()

# Withdraw Amount
if withdraw_amount <= balance:
    if is_govt_employee:
        if high_grade:
            balance = balance - withdraw_amount
            print("After withdraw:", balance)
        elif withdraw_amount + my_profit <= balance:
        	# Charging profit when user is a government employee and is less than grade 18
            balance = balance - (withdraw_amount + my_profit)
            print("After withdraw:", balance)
        else:
            print("Insufficient funds")
    elif is_senior_citizen or affiliated_card:
        balance = balance - withdraw_amount
        print("After withdraw:", balance)
    else:
        # Charging profit when user is not a senior citizen and user does not have affiliated card
        balance = balance - (withdraw_amount + my_profit)
        print("After withdraw:", balance)