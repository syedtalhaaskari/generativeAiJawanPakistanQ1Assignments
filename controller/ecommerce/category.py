from flask import Blueprint, request

from query import get_categories, insert_category

category = Blueprint('category', __name__)

@category.route('/api/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        try:
            categories = get_categories()
            # Fetch all categories
            if categories is None:
                raise Exception ('Something went wrong')
            return categories
        except Exception as e:
            return str(e), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()
            response = insert_category(data.get('category_name'))
            # Fetch all categories
            if response is not None:
                raise Exception (response)
            return 'Category Added Successfully', 200
        except Exception as e:
            return str(e), 500
    else:
        return 'Invalid request method', 405