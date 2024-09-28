from flask import Blueprint, request
import bcrypt 

signin = Blueprint('signin', __name__)

@signin.route('/signin', methods=['POST'])

def user_signin():
	try:
		users = [
			{
				"username": "talha",
				"password": b'$2b$12$5y4jYCCp/SkMVXOBcUjVNePwy5jgt.EA3wh/Xra/gsfzoPV.Grk5m'
			}
		]
		data = request.get_json()
		user_obj = {
			"username": data.get("username"),
			"password": data.get("password")
		}
		if user_obj['username'] is None or len(user_obj['username']) == 0:
				return 'Username is required', 400
		if user_obj['password'] is None or len(user_obj['password']) == 0:
				return 'Password is required', 400
		bytes = user_obj['password'].encode('utf-8') 
		for user in users:
			if user_obj['username'] == user['username'] and bcrypt.checkpw(bytes, user['password']):
				return 'User authenticated successfully', 200

		return 'Invalid Username or Password', 401
	except Exception as e:
	    return str(e), 500