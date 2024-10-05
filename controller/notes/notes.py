from datetime import datetime

from flask import Blueprint, request

from notes_query import get_session_by_id, delete_note, get_category_by_id, update_note, get_note_by_id, get_user_by_id, get_user_notes, insert_note

notes = Blueprint('notes', __name__)

@notes.route('/notes', methods=['GET', 'POST'])
def basic_note_operations():
    session_id = request.cookies.get('session_id')
    if session_id is None:
        return 'Please Login To Continue', 401
    session_obj = {
        "session_id": session_id,
        "ip_address": request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    }
    session_id_response = get_session_by_id(session_obj)
    now = datetime.now()
    if session_id_response is None or now >= session_id_response["expires_at"]:
        return 'Invalid User', 401
    user_id = session_id_response["user_id"]

    if request.method == 'GET':
        try:
            title = request.args.get("title")
            category_id = request.args.get("category_id")
            date_created = request.args.get("date_created")
            
            if category_id is not None:
                response = get_category_by_id(category_id)
                if response is None:
                    return 'Invalid Category ID', 400

            response_notes = get_user_notes(user_id, title, category_id, date_created)
            if response_notes is None:
                return [], 200
            return response_notes if len(response_notes) > 0 else [], 200
        except Exception as e:
            return str(e), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()
            note_obj = {
                "user_id": user_id,
                "title" : data.get('title'),
                "content" : data.get('content'),
                "category_id" : data.get('category_id')
            }
            if note_obj["title"] is None or len(note_obj["title"]) == 0:
                return 'Title is required', 400
            if note_obj["content"] is None or len(note_obj["content"]) == 0:
                return 'Content is required', 400

            if note_obj['category_id'] is not None:
                response = get_category_by_id(note_obj['category_id'])
                if response is None:
                    return 'Invalid Category ID', 400

            response = insert_note(note_obj)
            if response == True:
                return 'Note Created Successfully', 201
            raise Exception (response)
        except Exception as e:
            return str(e), 500

@notes.route('/notes/<int:note_id>', methods=['GET', 'PUT', 'DELETE'])
def delete_update_note_operations(note_id):
    session_id = request.cookies.get('session_id')
    if session_id is None:
        return 'Please Login To Continue', 401
    session_obj = {
        "session_id": session_id,
        "ip_address": request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    }
    session_id_response = get_session_by_id(session_obj)
    now = datetime.now()
    if session_id_response is None or now >= session_id_response["expires_at"]:
        return 'Invalid User', 401
    user_id = session_id_response["user_id"]

    response_note = get_note_by_id(user_id, note_id)
    
    if response_note is None:
        return 'Invalid Note ID', 400
    
    if request.method == 'GET':
        return response_note, 200
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            title = data.get('title')
            content = data.get('content')
            category_id = data.get('category_id')
            note_obj = {
                "user_id": user_id,
                "title" : title,
                "content" : content,
                "category_id" : category_id,
                "note_id" : note_id
            }

            if category_id is not None:
                response = get_category_by_id(category_id)
                if response is None:
                    return 'Invalid Category ID', 400
                note_obj['category_id'] = category_id if category_id is not None else response.get('category_id')
            if note_obj["title"] is None or len(note_obj["title"]) == 0:
                return 'Title is required', 400
            if note_obj["content"] is None or len(note_obj["content"]) == 0:
                return 'Content is required', 400

            note_obj['title'] = title if title is not None else response_note.get('title')
            note_obj['content'] = content if content is not None else response_note.get('content')
            
            response = update_note(note_obj)
            if response is not True:
                raise Exception (response)
            return 'Note Updated Successfully', 200
        except Exception as e:
            return str(e), 500
    elif request.method == 'DELETE':
        try:
            response = delete_note(user_id, note_id)
            if response == True:
                return 'Note Deleted Successfully', 200
            raise Exception ("Something went wrong")
        except Exception as e:
            return str(e), 500