import inquirer
import os
import json

import db
from query import insert_category, add_product_by_name, update_product_name_by_id, delete_product_by_id, get_categories, get_products, get_categories_and_products

from add_data_functions import add_category, add_user, add_product, add_order, add_payment

db_conn = db.mysqlconnect()

def print_mysql_data(data):
    print(
	  	json.dumps(data, default=str, indent=4)
	)



# def add_product():
#     product_name = input("Please enter product name: ")
#     cat_id = int(input("Please enter cat_id: ")) or 0
#     add_product_by_name(db_conn, product_name, cat_id)

def update_product():
	product_name = input("Please enter product new name: ")
	product_id = int(input("Please enter product id: ")) or 0
	update_product_name_by_id(db_conn, product_name, product_id)
 
def delete_product():
	product_id = int(input("Please enter product id: ")) or 0
	delete_product_by_id(db_conn, product_id)

def display_categories():
	categories = get_categories(db_conn)
	print_mysql_data(categories)

def display_products():
	products = get_products(db_conn)
	print_mysql_data(products)

def display_products_and_categories():
    products_and_categories = get_categories_and_products(db_conn)
    print_mysql_data(products_and_categories)
  
# options = (
# 	add_category,
#  	add_product,
#  	update_product,
#  	delete_product,
#  	display_categories,
#  	display_products,
#  	display_products_and_categories,
# )

# def homepage():
#     print()
#     question = [
#         inquirer.List('choice',
#             message="What action do you want to perform",
#             choices=[
#                 ('1. Add Categories', 0),
#                 ('2. Add Products', 1),
#                 ('3. Update Product', 2),
#                 ('4. Delete Product', 3),
#                 ('5. Display All Categories', 4),
#                 ('6. Display All Products', 5),
#                 ('7. Display Both Product and Categories Combine', 6),
#                 ('8. Exit', 7),
#             ],
#         ),
#     ]
    
#     answer = inquirer.prompt(question)
    
#     choice = answer['choice']
    
#     if choice == 7:
#         db.disconnect(db_conn)
#         exit(0)
  
#     options[choice]()

def sales_metrics():
    print()
    question = [
        inquirer.List('choice',
            message="Please Select",
            choices=[
                ('1. Total Revenue', 0),
                ('2. Revenue by Product', 1),
                ('3. Top Selling Products', 2),
                ('4. Revenue by Region/City', 3),
                ('5. Back', 4),
                ('6. Back to Main Menu', 5),
                ('7. Exit', 6),
            ],
        ),
    ]
    
    answer = inquirer.prompt(question)
    
    choice = answer['choice']
    if choice == 4:
        clear_console()
        display_stats()
    elif choice == 5:
        clear_console()
        homepage()
    elif choice == 6:
        clear_console()
        db.disconnect(db_conn)
        exit(0)
    else:
        sales_metrics_options[choice]()
    
def display_stats():
    print()
    question = [
        inquirer.List('choice',
            message="What action do you want to perform",
            choices=[
                ('1. Sales Metrics', 0),
                ('2. Order Metrics', 1),
                ('3. Payment Metrics', 2),
                ('4. Product Metrics', 3),
                ('5. Geographical Metrics', 4),
                ('6. Back to Main Menu', 5),
                ('7. Exit', 6),
            ],
        ),
    ]
    
    answer = inquirer.prompt(question)
    
    choice = answer['choice']
    if choice == 5:
        clear_console()
        homepage()
    elif choice == 6:
        clear_console()
        db.disconnect(db_conn)
        exit(0)
    else:
        stats_options[choice]()

def add_data():
    print()
    question = [
        inquirer.List('choice',
            message="What action do you want to perform",
            choices=[
                ('1. Add Category', 0),
                ('2. Add Product', 1),
                ('3. Add Customer', 2),
                ('4. Add Order', 3),
                ('5. Add Payment', 4),
                ('6. Back to Main Menu', 5),
                ('7. Exit', 6),
            ],
        ),
    ]
    
    answer = inquirer.prompt(question)
    
    choice = answer['choice']
    if choice == 5:
        clear_console()
        homepage()
    elif choice == 6:
        clear_console()
        db.disconnect(db_conn)
        exit(0)
    else:
        data_options[choice]()

sales_metrics_options = (
	add_category,
 	add_product,
 	add_user,
    add_order,
 	add_payment
)
data_options = (
	add_category,
 	add_product,
 	add_user,
    add_order,
 	add_payment
)
  
stats_options = (
	sales_metrics,
 	add_product,
 	update_product,
 	delete_product,
 	display_categories,
 	display_products,
 	display_products_and_categories,
)

def homepage():
    print()
    question = [
        inquirer.List('choice',
            message="Please Select",
            choices=[
                ('1. Add Data', 0),
                ('2. Display Stats', 1),
                ('3. Exit', 2),
            ],
        ),
    ]
    
    answer = inquirer.prompt(question)
    
    choice = answer['choice']
    
    if choice == 0:
        clear_console()
        add_data()
    elif choice == 1:
        clear_console()
        display_stats()
    elif choice == 2:
        db.disconnect(db_conn)
        exit(0)

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

clear_console()
while True:
	homepage()