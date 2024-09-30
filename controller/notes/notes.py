from flask import Blueprint, request

from query import get_categories, insert_category

notes = Blueprint('notes', __name__)

@notes.route('/notes', methods=['GET', 'POST'])
def basic_note_operations():
    if request.method == 'GET':
        try:
            title = request.args.get("title")
            category_id = request.args.get("category_id")
            date_created = request.args.get("date_created")
            return [], 200
            # Fetch all categories
            # if categories is None:
            #     raise Exception ('Something went wrong')
            # return categories if len(categories) > 0 else [], 200
        except Exception as e:
            return str(e), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()
            title = data.get('title')
            content = data.get('content')
            category_id = data.get('category_id')
            if title is None or len(title) == 0:
                return 'Title is required', 400
            if content is None or len(content) == 0:
                return 'Content is required', 400

            response = insert_category(data.get('category_name'))
            # Fetch all categories
            if response is not None:
                raise Exception (response)
            return 'Note Created Successfully', 201
        except Exception as e:
            return str(e), 500

@notes.route('/notes/<int:note_id>', methods=['PUT', 'DELETE'])
def delete_update_note_operations(note_id):
    if request.method == 'PUT':
        try:
            data = request.get_json()
            title = data.get('title')
            content = data.get('content')
            category_id = data.get('category_id')
            if (title is not None and len(title) == 0) or (content is not None and len(content) == 0) or (category_id is not None and len(category_id) == 0):
                return 'Provided fields should have length greater than zero', 400

            response = insert_category(data.get('category_name'))
            # Fetch all categories
            if response is not None:
                raise Exception (response)
            return 'Note Updated Successfully', 200
        except Exception as e:
            return str(e), 500
    elif request.method == 'DELETE':
        try:
            if len(note_id) == 0:
                return 'Note ID is required', 400

            response = insert_category(data.get('category_name'))
            # Fetch all categories
            if response is not None:
                raise Exception (response)
            return 'Note Deleted Successfully', 200
        except Exception as e:
            return str(e), 500