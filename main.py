import inquirer
import os
import json

from query import add_category_by_name, add_product_by_name, update_product_name_by_id, delete_product_by_id, get_categories, get_products, get_categories_and_products

def print_mysql_data(data):
    print(
	  	json.dumps(data, default=str, indent=4)
	)

def add_category():
    category_name = input("Please enter category name: ")
    add_category_by_name(category_name)

def add_product():
    product_name = input("Please enter product name: ")
    cat_id = int(input("Please enter cat_id: ")) or 0
    add_product_by_name(product_name, cat_id)

def update_product():
	product_name = input("Please enter product new name: ")
	product_id = int(input("Please enter product id: ")) or 0
	update_product_name_by_id(product_name, product_id)
 
def delete_product():
	product_id = int(input("Please enter product id: ")) or 0
	delete_product_by_id(product_id)

def display_categories():
	categories = get_categories()
	print_mysql_data(categories)

def display_products():
	products = get_products()
	print_mysql_data(products)

def display_products_and_categories():
    products_and_categories = get_categories_and_products()
    print_mysql_data(products_and_categories)
  
options = (
	add_category,
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
            message="What action do you want to perform",
            choices=[
                ('1. Add Categories', 0),
                ('2. Add Products', 1),
                ('3. Update Product', 2),
                ('4. Delete Product', 3),
                ('5. Display All Categories', 4),
                ('6. Display All Products', 5),
                ('7. Display Both Product and Categories Combine', 6),
                ('8. Exit', 7),
            ],
        ),
    ]
    
    answer = inquirer.prompt(question)
    
    choice = answer['choice']
    
    if choice == 7:
        exit(0)
  
    options[choice]()

os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    while True:
        homepage()