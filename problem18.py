"""
Write a program that takes the total amount of a purchase as input and applies a discount:

If the amount is less than $100, no discount.
If the amount is between $100 and $500, apply a 10% discount.
If the amount is more than $500, apply a 20% discount.
Print the final amount after the discount.
"""

purchase = int(input("Enter total amount of purchase: "))

if purchase < 100 and purchase > 0:
    print("No discount.")
elif purchase <= 500 and purchase >= 100:
    discount = purchase  * 0.1
    total = purchase - discount
    print("Final amount of purchase:", total)
elif purchase > 500:
    discount = purchase  * 0.2
    total = purchase - discount
    print("Final amount of purchase:", total)
else:
    print("Invalid Input")