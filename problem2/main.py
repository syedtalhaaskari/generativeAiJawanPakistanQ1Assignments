"""
Problem 1:

create class Item
add instance properties
  name, price, quantity
create method calcualte_total_price
create method apply_discount
create method all_items

all items have 20% discount by default

# use these items and store it in items.csv
"Phone", 100, 1
"Laptop", 1000, 3
"Cable", 10, 5
"Mouse", 50, 5
"Keyboard", 75, 5

# read items.csv and create objects for each item
# I should be able to print all the items


# Problem 2:
# extend the above application
restrict updating the price directly i.e item.price = 100
"""

from item import Item
    
Item.instanciate_from_csv()

items = Item.all

for (i, item_obj) in enumerate(items):
    print('--------------------------------')
    print(f"Name: {item_obj.name}")
    print(f"Price: {item_obj.price}")
    print(f"Quantity: {item_obj.quantity}")
    item_obj.apply_discount()
    print(f"Price after discount: {item_obj.price}")
    print(f"Total Price: {item_obj.calculate_total_price()}")
    print('--------------------------------')