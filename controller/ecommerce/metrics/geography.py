from flask import Blueprint, request

from metrics_query import get_top_cities_by_sales, get_top_countries_by_sales

geography = Blueprint('geography', __name__)

@geography.route('/api/metrics/geography', methods=['GET'])
def geography_metrics():
    try:
        top_cities_by_sales = get_top_cities_by_sales()
        top_countries_by_sales = get_top_countries_by_sales()
        if top_cities_by_sales is None or top_countries_by_sales is None:
            raise Exception ('Something went wrong')
        return {
        	'top_cities_by_sales': top_cities_by_sales if len(top_cities_by_sales) > 0 else [],
        	'top_countries_by_sales': top_countries_by_sales if len(top_countries_by_sales) > 0 else []
		}, 200
    except Exception as e:
        return str(e), 500