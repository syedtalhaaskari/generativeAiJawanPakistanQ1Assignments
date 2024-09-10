import inquirer
import re
from tabulate import tabulate

import db
from query import insert_category, insert_user, get_categories, insert_product, get_products, get_users, insert_order, insert_order_details, insert_payment, update_total_amount_and_payment_id_in_order, get_orders_by_user_id, get_order_details_by_order_id, get_products_by_order_id_and_user_id

db_conn = db.mysqlconnect()

def fetch_users():
    users = get_users(db_conn)
    list_users = []
    for user in users:
        list_users.append((f"{user['first_name']} {user['last_name']}", user))
    return list_users

def fetch_products():
    products = get_products(db_conn)
    list_products = []
    for product in products:
        list_products.append((product['product_name'], product))
    return list_products

def fetch_categories():
    categories = get_categories(db_conn)
    list_categories = []
    for category in categories:
        list_categories.append((category['category_name'], category['id']))
    return list_categories

def required_field_validation(answer, current):
    if len(current) == 0:
        raise inquirer.errors.ValidationError("", reason="This is a required field")
    return True

def length_validation(answer, current, length = 0):
    if len(current) > length:
        raise inquirer.errors.ValidationError("", reason=f"Length of this field should be less than or equal to {length}")
    return True

def number_validation(answer, current):
    if not re.match(r"[+-]?\d", current):
        raise inquirer.errors.ValidationError("", reason=f"This field must be a number")
    if float(current) <= 0:
        raise inquirer.errors.ValidationError("", reason=f"This field must be greater than 0")
    return True

def max_number_validation(answer, current, max_limit):
    if int(current) > max_limit:
        raise inquirer.errors.ValidationError("", reason=f"This field must be less than or equal to {max_limit}")
    return True

def add_category():
    question = [
        inquirer.Text(
            'category_name',
            message='Please enter category name',
            validate=required_field_validation,
        ),
    ]
    answer = inquirer.prompt(question)
    category_name = answer['category_name']
    insert_category(db_conn, category_name)

def add_user():
    question = [
        inquirer.Text(
            'first_name',
            message='Please enter your first name',
            validate=lambda ans, cur : (required_field_validation(ans, cur), length_validation(ans, cur, 45)),
        ),
        inquirer.Text(
            'last_name',
            message='Please enter your last name',
            validate=lambda ans, cur : length_validation(ans, cur, 45),
        ),
        inquirer.Text(
            'email',
            message='Please enter your email',
            validate=lambda ans, cur : (required_field_validation(ans, cur), length_validation(ans, cur, 45)),
        ),
        inquirer.Text(
            'phone_number',
            message='Please enter your phone number',
            validate=lambda ans, cur : (required_field_validation(ans, cur), length_validation(ans, cur, 25)),
        ),
        inquirer.Text(
            'address',
            message='Please enter your address',
            validate=lambda ans, cur : (required_field_validation(ans, cur), length_validation(ans, cur, 200)),
        ),
        inquirer.Text(
            'city',
            message='Please enter your city',
            validate=lambda ans, cur : (required_field_validation(ans, cur), length_validation(ans, cur, 45)),
        ),
        inquirer.Text(
            'country',
            message='Please enter your country',
            validate=lambda ans, cur : (required_field_validation(ans, cur), length_validation(ans, cur, 45)),
        ),
    ]
    
    answers = inquirer.prompt(question)
    insert_user(db_conn, answers)
    print('User Added Successfully')

def add_product():
    question = [
        inquirer.Text(
            'product_name',
            message='Please enter product name',
            validate=lambda ans, cur : (required_field_validation(ans, cur), length_validation(ans, cur, 45)),
        ),
        inquirer.Text(
            'product_details',
            message='Please enter product details',
            validate=lambda ans, cur : (required_field_validation(ans, cur), length_validation(ans, cur, 300)),
        ),
        inquirer.Text(
            'price',
            message='Please enter price',
            validate=lambda ans, cur : (required_field_validation(ans, cur), number_validation(ans, cur)),
        ),
        inquirer.Text(
            'quantity',
            message='Please enter quantity',
            validate=lambda ans, cur : (required_field_validation(ans, cur), number_validation(ans, cur)),
        ),
        inquirer.List(
            'category_id',
            message="Please select a category",
            choices=fetch_categories(),
        ),
    ]
    answers = inquirer.prompt(question)

    insert_product(db_conn, answers)
    print('Product Added Successfully')

def add_order():
    question_1 = [
        inquirer.List(
            'user',
            message='Please Select Customer',
            choices=fetch_users(),
        ),
        inquirer.Checkbox(
            'products',
            message='Please Select Product(s) - Press space to select',
            choices=fetch_products(),
            validate=required_field_validation,
        )
    ]
    answers_1 = inquirer.prompt(question_1)
    
    question_2 = []
    for item in answers_1["products"]:
        quantity = item["quantity"]
        question_2.append(
            inquirer.Text(
                'quantity'+ str(item['id']),
                message=f'Product: {item["product_name"]} > Please enter quantity (Available: {quantity})',
                validate=lambda ans, cur, quantity = quantity: (required_field_validation(ans, cur), number_validation(ans, cur), max_number_validation(ans, cur, quantity)),
            ) 
        )
    
    answers_2 = inquirer.prompt(question_2)

    order_obj = {
        "user_id": answers_1['user']["id"],
        "shipping_address": answers_1['user']["address"],
        "city": answers_1['user']["city"],
        "country": answers_1['user']["country"],
    }
    
    order_details_list = []

    order_id = insert_order(db_conn, order_obj)
    for product in answers_1['products']:
        order_details_list.append({
            "order_id": order_id,
            "product_id": product["id"],
            "price": product["price"],
            "quantity": answers_2['quantity'+ str(product['id'])],
        })

    total_amount = insert_order_details(db_conn, order_details_list)
    
    payment_obj = {
        'total_amount': total_amount,
        'order_id': order_id,
    }
    payment_id = insert_payment(db_conn, payment_obj)
    
    update_total_amount_and_payment_id_in_order(db_conn, order_id, total_amount, payment_id)
    
    print('Order Added Successfully')
    print('Please proceed to payment to confirm the order')
    
def add_payment():
    questions_1 = [
        inquirer.List(
            'user',
            message='Please Select Customer',
            choices=fetch_users(),
        ),
        # inquirer.Checkbox(
        #     'payment_method',
        #     message='Please select payment method:',
        #     choices=[
        #         'Cash',
        #         'Card'
        #     ]
        # )
    ]
    answers_1 = inquirer.prompt(questions_1)

    user_id = answers_1['user']['id']

    order_ids = [order['id'] for order in get_orders_by_user_id(db_conn, answers_1['user']['id'])]
    # print('orders id ', order_ids)
    
    orders = []
    for order_id in order_ids:
        orders.append(get_products_by_order_id_and_user_id(db_conn, order_id, user_id))
    # order_details = get_order_details_by_order_id(db_conn, order_id)
    # product_ids = tuple([order_item['product_id'] for order_item in order_details])
    order_item_questions = []
    # print('orders ', orders)
    for order in orders:
        header = order[0].keys()
        rows =  [x.values() for x in order]
        # print('header ', header)
        # print('rows ', rows)
        # for order_item in order:
        #     print(order_item)
        #     print()
        # print(tabulate(rows, header))
        order_item_questions.append((tabulate(rows, header, tablefmt="grid"), order[0]['order_id']))

    questions_2 = [
        inquirer.Checkbox(
            'payment_method',
            message='Please select payment method:',
            choices=order_item_questions
        )
    ]
    answers_2 = inquirer.prompt(questions_2)
    # questions = [
    #     inquirer.List(
    #         'user',
    #         message='Please Select Customer',
    #         choices=fetch_users(),
    #     ),
    # ]