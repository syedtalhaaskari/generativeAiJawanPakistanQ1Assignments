from flask import Blueprint, request

from metrics_query import get_total_revenue, get_this_month_top_selling_products, get_revenue_by_city, get_revenue_by_product

sales = Blueprint('sales', __name__)

@sales.route('/api/metrics/sales', methods=['GET'])
def sales_metrics():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        total_revenue = get_total_revenue()
        this_month_top_selling_products = get_this_month_top_selling_products()
        revenue_by_city = get_revenue_by_city(start_date, end_date)
        revenue_by_product = get_revenue_by_product(start_date, end_date)
        if total_revenue is None or this_month_top_selling_products is None or revenue_by_city is None or revenue_by_product is None:
            raise Exception ('Something went wrong')
        return {
        	'total_revenue': total_revenue if len(total_revenue) > 0 else [],
        	'this_month_top_selling_products': this_month_top_selling_products if len(this_month_top_selling_products) > 0 else [],
        	'revenue_by_city': revenue_by_city if len(revenue_by_city) > 0 else [],
        	'revenue_by_product': revenue_by_product if len(revenue_by_product) > 0 else []
		}, 200
    except Exception as e:
        return str(e), 500