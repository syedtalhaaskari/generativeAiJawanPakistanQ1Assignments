from flask import Blueprint, request
import bcrypt 

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
		# response = insert_category(data.get('category_name'))
		# Fetch all categories
		# if response is not None:
		print(user_obj)
		print(b'$2b$12$5y4jYCCp/SkMVXOBcUjVNePwy5jgt.EA3wh/Xra/gsfzoPV.Grk5m' == user_obj['password'])
	    #     raise Exception (response)
		return 'User Signup Successfully', 201
	except Exception as e:
	    return str(e), 500