from flask import Blueprint, request, make_response
import bcrypt 

from notes_query import get_user

signin = Blueprint('signin', __name__)

@signin.route('/signin', methods=['POST'])

def user_signin():
	try:
		ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
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
			resp = make_response('User authenticated successfully')
			resp.set_cookie('user_id', str(response['id']))
			return resp, 200

		return 'Invalid Username or Password', 401
	except Exception as e:
	    return str(e), 500