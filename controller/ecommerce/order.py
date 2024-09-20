from flask import Blueprint, request

from query import get_products, insert_product

order = Blueprint('order', __name__)

@order.route('/api/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        try:
            orders = get_products()
            # Fetch all orders
            if orders is None:
                raise Exception ('Something went wrong')
            return orders
        except Exception as e:
            return str(e), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()
            product_obj = {
                "product_name": data.get('product_name'),
                "product_details": data.get('product_details'),
                "price": data.get('price'),
                "quantity": data.get('quantity'),
                "category_id": data.get('category_id'),
            }
            response = insert_product(product_obj)
            # Fetch all orders
            if response is not None:
                raise Exception (response)
            return 'Order Added Successfully', 200
        except Exception as e:
            return str(e), 500
    else:
        return 'Invalid request method', 405