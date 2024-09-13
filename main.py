import inquirer
import os
import json

import db
from query import insert_category, add_product_by_name, update_product_name_by_id, delete_product_by_id, get_categories, get_products, get_categories_and_products

from add_data_functions import add_category, add_user, add_product, add_order, add_payment
from show_metrics_functions import print_top_cities_by_sales, print_top_countries_by_sales, print_inventory_levels, print_out_of_stock_products, print_payment_metrics, print_order_metrics, print_this_month_top_selling_products, print_revenue_by_product, print_revenue_by_city, print_total_revenue

db_conn = db.mysqlconnect()

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

def product_metrics():
    print()
    question = [
        inquirer.List('choice',
            message="Please Select",
            choices=[
                ('1. Inventory Levels (Overall)', 0),
                ('2. Out of Stock Products', 1),
                ('5. Back', 2),
                ('6. Back to Main Menu', 3),
                ('7. Exit', 4),
            ],
        ),
    ]
    
    answer = inquirer.prompt(question)
    
    choice = answer['choice']
    if choice == 2:
        clear_console()
        display_stats()
    elif choice == 3:
        clear_console()
        homepage()
    elif choice == 4:
        clear_console()
        db.disconnect(db_conn)
        exit(0)
    else:
        product_metrics_options[choice]()

def geographical_metrics():
    print()
    question = [
        inquirer.List('choice',
            message="Please Select",
            choices=[
                ('1. Top Cities by Sales (This Month)', 0),
                ('2. Top Countries by Sales (This Month)', 1),
                ('5. Back', 2),
                ('6. Back to Main Menu', 3),
                ('7. Exit', 4),
            ],
        ),
    ]
    
    answer = inquirer.prompt(question)
    
    choice = answer['choice']
    if choice == 2:
        clear_console()
        display_stats()
    elif choice == 3:
        clear_console()
        homepage()
    elif choice == 4:
        clear_console()
        db.disconnect(db_conn)
        exit(0)
    else:
        geographical_metrics_options[choice]()
    
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
	print_total_revenue,
 	print_revenue_by_product,
 	print_this_month_top_selling_products,
    print_revenue_by_city
)

product_metrics_options = (
    print_inventory_levels,
    print_out_of_stock_products
)

geographical_metrics_options = (
    print_top_cities_by_sales,
    print_top_countries_by_sales
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
 	print_order_metrics,
 	print_payment_metrics,
 	product_metrics,
 	geographical_metrics
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