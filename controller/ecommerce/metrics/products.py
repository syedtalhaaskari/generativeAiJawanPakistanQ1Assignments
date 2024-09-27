from flask import Blueprint, request

from metrics_query import get_inventory_levels, get_out_of_stock_products

products = Blueprint('products', __name__)

@products.route('/api/metrics/products', methods=['GET'])
def products_metrics():
    try:
        inventory_levels = get_inventory_levels()
        out_of_stock_products = get_out_of_stock_products()
        if inventory_levels is None or out_of_stock_products is None:
            raise Exception ('Something went wrong')
        return {
        	'inventory_levels': inventory_levels if len(inventory_levels) > 0 else [],
        	'out_of_stock_products': out_of_stock_products if len(out_of_stock_products) > 0 else []
		}, 200
    except Exception as e:
        return str(e), 500