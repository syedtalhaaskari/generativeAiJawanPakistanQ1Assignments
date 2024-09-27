from flask import Blueprint, request

from metrics_query import get_order_metrics

orders = Blueprint('orders', __name__)

@orders.route('/api/metrics/orders', methods=['GET'])
def orders_metrics():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        order_metrics = get_order_metrics(start_date, end_date)
        if order_metrics is None:
            raise Exception ('Something went wrong')
        return order_metrics if len(order_metrics) > 0 else [], 200
    except Exception as e:
        return str(e), 500