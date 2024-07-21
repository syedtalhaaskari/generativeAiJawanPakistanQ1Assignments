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

class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.total_price = 0
        
    @property
    def price(self):
        return self.__price
    
    def calculate_total_price(self, discount = 0.2):
        discount = self.apply_discount(discount)
        self.total_price = ((float(self.price) - discount) * float(self.quantity))
        return self.total_price
    
    def apply_discount(self, discount_percentage=0.2):
        return float(self.price) * discount_percentage
    
    @staticmethod
    def all_items(filename: str):
        items = []
        with open(filename, 'r') as file:
            print("Name : Price : Quantity")
            for line in file:
                name, price, quantity = [item.strip() for item in line.strip().split(',')]
                name = name.replace("\"", "")
                separator()
                print("\nAll Items:")
                print(f"{name} : {price} : {quantity}")
                items.append([name, price, quantity])
            separator()
            print()
            file.close()
        
        return items
    
def separator():
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    
items = Item.all_items('data/items.csv')
items_obj = [None] * len(items)

for (i, (name, price, quantity)) in enumerate(items):
    separator()
    
    items_obj[i] = Item(name, price, quantity)
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Quantity: {quantity}")
    print(f"Discount/Item: {items_obj[i].apply_discount()}")
    print(f"Total Price: {items_obj[i].calculate_total_price()}")
    
    separator()