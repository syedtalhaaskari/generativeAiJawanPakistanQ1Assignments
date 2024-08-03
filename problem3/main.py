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


Problem 3:

# extend the above application
# There are extra attributes in laptop i.e gpu, port_count and also it has 30% discount

# application folder structure
1. items.py
2. laptop.py
3. data/items.csv

# use this link if you are unable to create the assignment even after taking help on the group
# use this link only on the next saturday
Ref: https://www.youtube.com/watch?v=Ej_02ICOIgs
"""

# from item import Item
from laptop import Laptop
    
# Item.instanciate_from_csv('data/items.csv')

# items = Item.all

# for (i, item_obj) in enumerate(items):
#     print('--------------------------------')
#     print(f"Name: {item_obj.name}")
#     print(f"Price: {item_obj.price}")
#     print(f"Quantity: {item_obj.quantity}")
#     item_obj.apply_discount()
#     print(f"Price after discount: {item_obj.price}")
#     print(f"Total Price: {item_obj.calculate_total_price()}")
#     print('--------------------------------')

laptop1 = Laptop('HP', 1000, 5, 2, 3)
laptop2 = Laptop('Apple', 3000, 2, 1, 2)
laptop3 = Laptop('Lenovo', 800, 10, 2, 4)

all_laptops = Laptop.all

for (i, laptop_obj) in enumerate(all_laptops):
    print('--------------------------------')
    print(f"Name: {laptop_obj.name}")
    print(f"Price: {laptop_obj.price}")
    print(f"Quantity: {laptop_obj.quantity}")
    print(f"GPU Count: {laptop_obj.gpu}")
    print(f"Port Count: {laptop_obj.port_count}")
    laptop_obj.apply_discount()
    print(f"Price after discount: {laptop_obj.price}")
    print(f"Total Price: {laptop_obj.calculate_total_price()}")
    print('--------------------------------')