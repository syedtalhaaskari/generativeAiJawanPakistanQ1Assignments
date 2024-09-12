import inquirer
import re
from tabulate import tabulate

import db
from query import update_order_status_after_payment_by_id, update_products_by_quantity, cancel_order, get_products_by_ids, get_available_products, insert_category, insert_user, get_categories, insert_product, get_products, get_users, insert_order, insert_order_details, insert_payment, update_total_amount_and_payment_id_in_order, get_orders_by_user_id, get_order_details_by_order_id, get_products_by_order_id_and_user_id, get_unpaid_orders_by_user_id, update_payment_by_id

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

def fetch_available_products():
    products = get_available_products(db_conn)
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
            choices=fetch_available_products(),
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
    users = fetch_users()

    if len(users) == 0:
        print('No customers found.')
        return

    questions_1 = [
        inquirer.List(
            'user',
            message='Please Select Customer',
            choices=fetch_users(),
        ),
    ]
    answers_1 = inquirer.prompt(questions_1)

    user_id = answers_1['user']['id']

    fetched_orders = get_unpaid_orders_by_user_id(db_conn, user_id)

    if len(fetched_orders) == 0:
        print('No unpaid orders found for the selected customer.')
        return
    
    orders = []
    for order in fetched_orders:
        orders.append(
            (f"""Id: {order['id']}, Total Amount: {order['total_amount']}, Payment Status: {order['order_status']}, Created At: {order['order_date']}""", order)
        )
    order_item_questions = [
        inquirer.List(
            'order',
            message='Please Select Order To Pay',
            choices=orders,
        ),
    ]
    answers_2 = inquirer.prompt(order_item_questions)

    order_id = answers_2['order']['id']

    order_details = get_order_details_by_order_id(db_conn, order_id)

    product_ids = str([order_detail['product_id'] for order_detail in order_details]).replace('[', '(').replace(']', ')')
    products = get_products_by_ids(db_conn, product_ids)

    for product in products:
        ind  = next((i for i, item in enumerate(order_details) if item["product_id"] == product['id']), None)
        if product['quantity'] == 0 or product['quantity'] < order_details[ind]['quantity']:
            cancel_order(db_conn, order_id)
            print(f'Payment failed and Order is cancelled for product {product["product_name"]}. Quantity is not available.')
            return
        
    questions_3 = [
        inquirer.List(
            'payment_method',
            message='Please select payment method:',
            choices=[
                'Cash',
                'Card'
            ]
        )
    ]
    answers_3 = inquirer.prompt(questions_3)
    payment_method = answers_3['payment_method']

    payment_obj = {
        'order_id': order_id,
        'payment_method': payment_method,
        'payment_status': 'Paid',
        'user_id': user_id,
        'total_amount': answers_2['order']['total_amount'],
    }

    update_payment_by_id(db_conn, payment_obj)
    update_order_status_after_payment_by_id(db_conn, order_id)
    update_products_by_quantity(db_conn, order_details)

    print('Payment Successful')