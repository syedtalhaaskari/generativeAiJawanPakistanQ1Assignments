from flask import Blueprint, request

from query import get_users, insert_user

customer = Blueprint('customer', __name__)

@customer.route('/api/customers', methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        try:
            customers = get_users()
            # Fetch all customers
            if customers is None:
                raise Exception ('Something went wrong')
            return customers if len(customers) > 0 else [], 200
        except Exception as e:
            return str(e), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()
            customer_obj = {
                "first_name": data.get('first_name'),
                "last_name": data.get('last_name'),
                "email": data.get('email'),
                "phone_number": data.get('phone_number'),
                "address": data.get('address'),
                "city": data.get('city'),
                "country": data.get('country'),
            }
            response = insert_user(customer_obj)
            # Fetch all customers
            if response is not None:
                raise Exception (response)
            return 'Customer Added Successfully', 201
        except Exception as e:
            return str(e), 500