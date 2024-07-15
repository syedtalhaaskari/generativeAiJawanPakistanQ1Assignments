# Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, quantity, price):
        print(f"\nItem to add => {name} : {quantity} : ${price}")
        self.items.append({
            'name': name,    
            'quantity': quantity,
            'price': price,
        })
        print("Item Added Successfully")
    
    def remove_item(self, name, quantity):
        print(f"\nItem to remove => {name} : {quantity}")
        for item in self.items:
            if item['name'] == name:
                if item['quantity'] >= quantity:
                    item['quantity'] -= quantity
                    print("Item Removed Successfully")
                    if item['quantity'] == 0:
                        self.items.remove(item)
                else:
                    print(f"Not enough {name} in the cart.")
                return
    
    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item['price'] * item['quantity']
        print(f"\nTotal Price: {total_price}")
    
    def display_items(self):
        print("\nShopping Cart Items => Name : Quantity : Price")
        for item in self.items:
            print(f"{item['name']} : {item['quantity']} : ${item['price']}")
            
my_cart = ShoppingCart()

my_cart.add_item("Apple", 5, 0.50)

my_cart.add_item("Banana", 3, 0.30)

my_cart.display_items()

my_cart.remove_item("Apple", 2)

my_cart.display_items()

my_cart.calculate_total_price()