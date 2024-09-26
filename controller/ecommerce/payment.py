from flask import Blueprint, request

from query import update_payment_by_id, update_order_status_after_payment_by_id, update_products_by_quantity, cancel_order, get_products_by_ids, get_order_details_by_order_id, get_user_by_id

payment = Blueprint('payment', __name__)

@payment.route('/api/payments', methods=['POST'])
def payments():
    try:
        data = request.get_json()
        payment_obj = {
            "user_id": data.get('user_id'),
            "order_id": data.get('order_id'),
            "payment_method": data.get('payment_method'),
            "payment_status": 'Paid',
            "total_amount": 0,
        }
        if payment_obj['user_id'] is None:
            return 'user_id is required', 400
        elif payment_obj['order_id'] is None:
            return 'order_id is required', 400
        elif payment_obj['payment_method'] is None:
            return 'payment_method is required', 400

        user = get_user_by_id(payment_obj['user_id'])
        if len(user) == 0:
            return 'Invalid User Id', 400

        order_details = get_order_details_by_order_id(payment_obj['order_id'])
        if len(order_details) == 0:
            return 'Invalid Order Id', 400
        product_ids = str([order_detail['product_id'] for order_detail in order_details]).replace('[', '(').replace(']', ')')
        products = get_products_by_ids(product_ids)
        total_amount = 0
        for product in products:
            ind  = next((i for i, item in enumerate(order_details) if item["product_id"] == product['id']), None)
            if product['quantity'] == 0 or product['quantity'] < order_details[ind]['quantity']:
                cancel_order(payment_obj['order_id'])
                return f'Payment failed and Order is cancelled for product {product["product_name"]}. Quantity is not available.', 400
            total_amount += order_details[ind]['quantity'] * product['price']
        payment_obj['total_amount'] = total_amount
        update_payment_by_id(payment_obj)
        update_order_status_after_payment_by_id(payment_obj['order_id'])
        update_products_by_quantity(order_details)
        return 'Payment Added Successfully', 201
    except Exception as e:
        return str(e), 500