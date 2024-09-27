from flask import Blueprint, request

from metrics_query import get_payment_metrics

payments = Blueprint('payments', __name__)

@payments.route('/api/metrics/payments', methods=['GET'])
def payments_metrics():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        order_metrics = get_payment_metrics(start_date, end_date)
        if order_metrics is None:
            raise Exception ('Something went wrong')
        return order_metrics if len(order_metrics) > 0 else [], 200
    except Exception as e:
        return str(e), 500