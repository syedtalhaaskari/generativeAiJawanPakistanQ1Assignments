"""
Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:

If the customer is a member:
    If the purchase amount is $50 or more, print "Eligible for 10% discount".
    Otherwise, print "Eligible for 5% discount".
If the customer is not a member:
    If the purchase amount is $100 or more, print "Eligible for 5% discount".
    Otherwise, print "No discount".
"""

is_member = input("Are you a member(Y/N): ")[0].upper()
purchase_amount = int(input("Enter purchase amount: "))

if is_member == "Y":
    if purchase_amount >= 50:
        print("Eligible for 10% discount")
    else:
        print("Eligible for 5% discount")
elif is_member == "N":
    if purchase_amount >= 100:
        print("Eligible for 5% discount")
    else:
        print("No discount")
else:
    print("Invalid Input")