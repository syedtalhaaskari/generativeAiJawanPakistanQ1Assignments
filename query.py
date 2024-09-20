import pymysql
import db

def insert_category(category_name):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(
			f"""
			INSERT INTO Category 
			(
				category_name
			)
			VALUES (
				%(category_name)s
			)
			""", { 'category_name' : category_name })
		db_conn.commit()
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		db.disconnect()
  
def get_categories():
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM Category ORDER BY category_name")
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def insert_user(user_obj):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(
			f"""
			INSERT INTO User
			(
				first_name, last_name, email, phone_number, address, city, country
			)
			VALUES (
				'{user_obj['first_name']}',
				'{user_obj['last_name']}',
				'{user_obj['email']}',
				'{user_obj['phone_number']}',
				'{user_obj['address']}',
				'{user_obj['city']}',
				'{user_obj['country']}'
			)
			""")
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)    
    finally:
        db.disconnect()
        
def get_users():
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM User")
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def insert_product(product_obj):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(
			f"""
			INSERT INTO Product
			(
				product_name, product_details, price, quantity, category_id
			)
			VALUES (
				%(product_name)s,
				%(product_details)s,
				%(price)s,
				%(quantity)s,
				%(category_id)s
			)
			""", {
                "product_name" : product_obj['product_name'],
                "product_details" : product_obj['product_details'],
                "price" : product_obj['price'],
                "quantity" : product_obj['quantity'],
                "category_id" : product_obj['category_id']
            })
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()
        
def get_products():
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM Product")
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def get_available_products():
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM Product Where quantity > 0")
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def get_products_by_ids(product_ids):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(f"SELECT id, product_name, quantity FROM Product Where id IN {str(product_ids)}")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong,', e)
	finally:
		db.disconnect()

def insert_order(order_obj):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"""
			INSERT INTO Order_Table
			(
				user_id, shipping_address, city, country
			)
			VALUES (
				%(user_id)s,
				%(shipping_address)s,
				%(city)s,
				%(country)s
			);
		""", {
            "user_id" : order_obj["user_id"],
            "shipping_address" : order_obj["shipping_address"],
            "city" : order_obj["city"],
            "country" : order_obj["country"]
        })
        db_conn.commit()
        cur.execute("SELECT LAST_INSERT_ID() AS id;")
        return cur.fetchall()[0]['id']
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def cancel_order(order_id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"""
			Update Order_Table
			SET order_status = 'Cancelled'
            WHERE id = {order_id};
		""")
        cur.execute(f"""
			Update Payment
			SET payment_status = 'Cancelled'
            WHERE order_id = {order_id};
		""")
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def insert_order_details(order_details_list):
    query_string = ''
    total_amount = 0
    for order_obj in order_details_list: 
        total_amount += order_obj['price'] * float(order_obj['quantity'])
        query_string += f"""(
			{order_obj['order_id']},
			{order_obj['product_id']},
			{order_obj['price']},
			{order_obj['quantity']}
		),"""
    query_string = query_string[:-1]  # remove trailing comma
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"""
			INSERT INTO Order_Details
				(
					order_id, product_id, price, quantity
				)
			VALUES {query_string};
		""")
        db_conn.commit()
        return total_amount
    except pymysql.Error as e:
        print('Something went wrong,', e)  
    finally:
        db.disconnect()  

def update_products_by_quantity(order_details_list):
    try:
        db_conn = db.mysqlconnect()
        for order_obj in order_details_list:
            cur = db_conn.cursor()
            quantity = order_obj['quantity']
            id = order_obj['product_id']
            cur.execute(f"""
				UPDATE Product
				SET quantity = quantity - {quantity}
				WHERE id = {id};
			""")
            db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)   
    finally:
        db.disconnect()   

def insert_payment(payment_obj):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"""
			INSERT INTO Payment
			(
				total_amount, order_id
			)
			VALUES (
				%(total_amount)s,
				%(order_id)s
			);
		""", {
            "total_amount" : payment_obj["total_amount"],
            "order_id" : payment_obj["order_id"]
        })
        db_conn.commit()
        cur.execute("SELECT LAST_INSERT_ID() AS id;")
        return cur.fetchall()[0]['id']
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()
        
def update_total_amount_and_payment_id_in_order(order_id, total_amount, payment_id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"""
			UPDATE Order_Table
   			SET total_amount = %(total_amount)s, payment_id = %(payment_id)s
			WHERE id = %(order_id)s;
		""", {
            "order_id" : order_id,
            "total_amount" : total_amount,
            "payment_id" : payment_id
        })
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def get_orders_by_user_id(user_id):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(f"SELECT * FROM Order_Table WHERE user_id = %(user_id)s", { "user_id" : user_id })
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong,', e)
	finally:
		db.disconnect()

def get_order_details_by_order_id(order_id):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(f"SELECT * FROM Order_Details WHERE order_id = {order_id}")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong,', e)
	finally:
		db.disconnect()
  
def get_unpaid_orders_by_user_id(user_id):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(f"""
            SELECT
                o.id,
                o.order_date,
                o.order_status,
                o.total_amount
			FROM order_table o
			WHERE o.user_id = {user_id} AND o.order_status = 'Payment Pending';
        """)
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong,', e)
	finally:
		db.disconnect()

def update_order_status_after_payment_by_id(order_id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"""
            UPDATE Order_Table
            SET 
        		order_status='Delivered',
        		delivery_date=NOW()
			WHERE id = {order_id};
        """)
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def update_payment_by_id(payment_obj):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"""
            UPDATE Payment
            SET 
        		order_id={payment_obj['order_id']},
        		payment_method='{payment_obj['payment_method']}',
        		payment_status='{payment_obj['payment_status']}',
        		total_amount={payment_obj['total_amount']},
                payment_date=NOW()
			WHERE order_id = {payment_obj['order_id']};
        """)
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def get_products_by_order_id_and_user_id(order_id, user_id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"""
            SELECT
				od.order_id,
				p.product_name,
				od.price,
				od.quantity
			FROM order_table o
			JOIN order_details od
				ON od.order_id = o.id
			JOIN product p
				ON p.id = od.product_id
			WHERE o.user_id = {user_id} AND od.order_id = {order_id};
        """)
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()
  
def add_product_by_name(product_name, cat_id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(
			f"""
			INSERT INTO product 
			(
				name,
				cat_id
			)
			VALUES (
				'{product_name}',
				'{cat_id}'
			)
			""")
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()
 
def update_product_name_by_id(product_name, product_id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(
			f"""
			UPDATE product 
			SET name = '{product_name}'
			WHERE id = {product_id};
			""")
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()
 
def delete_product_by_id(product_id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"DELETE FROM product WHERE id = {product_id}")
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def get_products():
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM product")
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def get_categories_and_products():
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("""
			SELECT
				c.id AS category_id,
				c.name AS category_name,
				c.created_at AS category_created_at,
				p.id AS product_id,
				p.name AS product_name,
				p.created_at AS product_created_at,
				p.updated_at AS product_updated_at
			FROM category c
			LEFT JOIN product p
				ON c.id = p.cat_id;
		""")
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()