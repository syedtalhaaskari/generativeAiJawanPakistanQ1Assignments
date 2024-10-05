import uuid
from datetime import datetime, timedelta

from flask import Blueprint, request, make_response
import bcrypt

from notes_query import get_user, insert_session

signin = Blueprint('signin', __name__)

@signin.route('/signin', methods=['POST'])

def user_signin():
	try:
		data = request.get_json()
		username = data.get("username")
		password = data.get("password")
		if username is None or len(username) == 0:
				return 'Username is required', 400
		if password is None or len(password) == 0:
				return 'Password is required', 400
		bytes = password.encode('utf-8')
		response = get_user(username)

		if response is not None and bcrypt.checkpw(bytes, response['password']):
			ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
			session_id = uuid.uuid4()
			session_obj = {
				"session_id": str(session_id),
				"user_id": response['id'],
				"ip_address": ip_address,
			}
			session_resp = insert_session(session_obj)
			if session_resp is not None:
				resp = make_response('User authenticated successfully')
				resp.set_cookie(
        			'session_id', 
           			str(session_id),
                    expires=datetime.now() + timedelta(hours=1)
                )
				return resp, 200
			return "Something went wrong", 500

		return 'Invalid Username or Password', 401
	except Exception as e:
	    return str(e), 500