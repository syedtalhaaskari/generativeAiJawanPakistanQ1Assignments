from flask import Blueprint, request

from query import update_total_amount_and_payment_id_in_order, insert_payment, insert_order_details, get_orders_by_user_id, insert_order

order = Blueprint('order', __name__)

@order.route('/api/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        try:
            if user_id is None:
                raise Exception('User ID is required')
            orders = get_orders_by_user_id(user_id)
            # Fetch all orders
            if orders is None:
                raise Exception ('Something went wrong')
            return orders if len(orders) > 0 else []
        except Exception as e:
            return str(e), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()
            order_obj = {
                "user_id": data.get('user_id'),
                "shipping_address": data.get('shipping_address'),
                "city": data.get('city'),
                "country": data.get('country'),
            }
            order_details_obj = data.get('order_details')
            if order_details_obj is None or len(order_details_obj) <= 0:
                raise Exception('Order details are required')
            order_id = insert_order(order_obj)
            if not isinstance(order_id, (int, float, complex)) or isinstance(order_id, bool):
                raise Exception ('Something went wrong')
            for i in range(len(order_details_obj)):
                order_details_obj[i]['order_id'] = order_id

            total_amount = insert_order_details(order_details_obj)
            print("Otal ", total_amount)
            
            if not isinstance(total_amount, (int, float, complex)) or isinstance(total_amount, bool):
                raise Exception ('Something went wrong')
            
            payment_obj = {
                'total_amount': total_amount,
                'order_id': order_id,
            }
            payment_id = insert_payment(payment_obj)
            
            if not isinstance(payment_id, (int, float, complex)) or isinstance(payment_id, bool):
                raise Exception ('Something went wrong')

            update_total_amount_and_payment_id_in_order(order_id, total_amount, payment_id)
    
            return 'Order Added Successfully', 200
        except Exception as e:
            return str(e), 500
    else:
        return 'Invalid request method', 405