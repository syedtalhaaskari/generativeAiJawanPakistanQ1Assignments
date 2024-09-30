from flask import Blueprint, request
import bcrypt 

from notes_query import insert_user

signup = Blueprint('signup', __name__)

@signup.route('/signup', methods=['POST'])
def user_signup():
	try:
		data = request.get_json()
		user_obj = {
			"username": data.get("username"),
			"password": data.get("password")
		}
		if user_obj['username'] is None or len(user_obj['username']) == 0:
				return 'Username is required', 400
		if user_obj['password'] is None or len(user_obj['password']) == 0:
				return 'Password is required', 400

		# converting password to array of bytes
		bytes = user_obj['password'].encode('utf-8') 

		# generating the salt 
		salt = bcrypt.gensalt() 

		# Hashing the password 
		user_obj['password'] = bcrypt.hashpw(bytes, salt) 
		response = insert_user(user_obj)
		if response == True:
			return 'User Signup Successfully, Please Login to Continue', 201
		elif response.args[0] == 1062:
			return 'User already exists', 400
		else:
			raise Exception(response)
	except Exception as e:
	    return str(e), 500