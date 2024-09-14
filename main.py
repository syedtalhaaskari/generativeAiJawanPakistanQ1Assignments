from flask import Flask, request

from query import get_categories_and_products, delete_product_by_id, update_product_name_by_id, add_product_by_name, add_category_by_name, get_products, get_categories 

app = Flask(__name__)

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        fetched_categories = get_categories()
        return fetched_categories if len(fetched_categories) > 0 else []
    if request.method == 'POST':
        data = request.get_json()
        add_category_by_name(data['name'])
        return 'Category added successfully!'

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        fetched_products = get_products()
        return fetched_products if len(fetched_products) > 0 else []
    if request.method == 'POST':
        data = request.get_json()
        add_product_by_name(data['name'], data['category_id'])
        return 'Product added successfully!'

@app.route('/products/<int:id>', methods=['PUT', 'DELETE'])
def product(id):
    if request.method == 'PUT':
        data = request.get_json()
        update_product_name_by_id(data['new_name'], id)
        return 'Product updated successfully!'
    if request.method == 'DELETE':
        data = request.get_json()
        delete_product_by_id(id)
        return 'Product deleted successfully!'

@app.route('/products_and_categories', methods=['GET'])
def products_and_categories():
    if request.method == 'GET':
        fetched_items = get_categories_and_products()
        return fetched_items if len(fetched_items) > 0 else []

@app.route('/products_count', methods=['GET'])
def products_count():
    if request.method == 'GET':
        fetched_products = get_products()
        return str(len(fetched_products))

app.run(debug=True)