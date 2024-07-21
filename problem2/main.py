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

class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.total_price = 0
        
    @property
    def price(self):
        return self.__price
    
    def calculate_total_price(self):
        discount = self.apply_discount()
        self.total_price = (float(self.price) * float(self.quantity)) - discount
        return self.total_price
    
    def apply_discount(self, discount_percentage=0.2):
        perc = (1.0 - discount_percentage)
        return float(self.price) * perc
    
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
    
items = Item.all_items('items.csv')
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
    
    
