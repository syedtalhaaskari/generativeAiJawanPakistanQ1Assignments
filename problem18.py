"""
Take a variable store i.e
Store = {“name”: “my store”, “inventory”: [], “orders”: []}

Add 5 items in the inventory using a function “add_item”
id, name, price and quantity

Take user input unless it says “done”
Display user updated inventory items every time
Ask user to type id of the item to purchase or type “done” to checkout
Each time only 1 quantity will by subtracted from the item

Functions: add_item_in_inventory, add_item_in_basket(), checkout()
On checkout, print “{quantity} {item} sold in {store}”
"""

import copy
import pprint

def add_item_in_inventory(id, name, price, quantity):
    store['inventory'].append({'id': id, 'name': name, 'price': price, 'quantity': quantity})
    print("Updated inventory:")
    pprint.pp(store['inventory'])

def add_item_in_basket(id):
    for item in store['inventory']:
        if item['id'] == id:
            if item['quantity'] <= 1:
                for order_item in store['orders']:
                    if order_item['id'] == id:
                        return
                store['orders'].append(copy.deepcopy(item))
                store['orders'][len(store['orders']) - 1]['quantity'] = 1
            else:
                for order_item in store['orders']:
                    if order_item['id'] == id:
                        if order_item['quantity'] == item['quantity']:
                            return
                        order_item['quantity'] += 1
                        return
                
                store['orders'].append(copy.deepcopy(item))
                store['orders'][len(store['orders']) - 1]['quantity'] = 1    

def checkout():
    for order in store['orders']:
        pprint.pp(f'{order['quantity']} {order['name']} sold in {store}')
        
    for order in store['orders']:
        for item in store['inventory']:
            if item['id'] == order['id']:
                if item['quantity'] == order['quantity']:
                    store['inventory'].remove(item)
                    break
                else:
                    item['quantity'] -= order['quantity']
                    break
    
    store['orders'] = []

    print('\nAfter checkout:')
    pprint.pp(store)       
    pass

store = {
    'name': 'my store', 
    'inventory':  [
        # {'id': 0, 'name': 'Pakola', 'price': 60.0, 'quantity': 3},
        # {'id': 1, 'name': 'Anaar Juice', 'price': 90.0, 'quantity': 1},
        # {'id': 2, 'name': 'Cola Next', 'price': 100.0, 'quantity': 30},
        # {'id': 3, 'name': 'Fuzz Up', 'price': 100.0, 'quantity': 30},
        # {'id': 4, 'name': 'Protien', 'price': 200.0, 'quantity': 2},
    ],
    'orders': [], 
}

for i in range(5):
    id = len(store['inventory'])
    name = input('\nEnter name: ')
    price = abs(float(input('Enter price: ')))
    quantity = abs(int(input('Enter quantity: ')))
    add_item_in_inventory(id, name, price, quantity)

print("\nOrders:")
pprint.pp(store['orders'])
    
while True:
    print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    
    inp = input('Enter id of the item to purchase or type "done" to checkout: ') or -1
    
    if inp == 'done':
        checkout()
        break
    
    add_item_in_basket(int(inp))
    print("\nInventory:")
    pprint.pp(store['inventory'])
    print("\nOrders:")
    pprint.pp(store['orders'])