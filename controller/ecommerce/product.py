from flask import Blueprint, request

from query import get_products, insert_product

product = Blueprint('product', __name__)

@product.route('/api/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        try:
            query_category = request.args.get('category')
            products = get_products(query_category)
            # Fetch all products
            if products is None:
                raise Exception ('Something went wrong')
            return products if len(products) > 0 else [], 200
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
            # Fetch all products
            if response is not None:
                raise Exception (response)
            return 'Product Added Successfully', 201
        except Exception as e:
            return str(e), 500