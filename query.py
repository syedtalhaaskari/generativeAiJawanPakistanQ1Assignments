import pymysql

def insert_category(db_conn, category_name):
	cur = db_conn.cursor()
	try:
		cur.execute(
			f"""
			INSERT INTO Category 
			(
				category_name
			)
			VALUES (
				'{category_name}'
			)
			""")
		db_conn.commit()
	except pymysql.Error as e:
		print('Something went wrong,', e)
  
def get_categories(db_conn):
	cur = db_conn.cursor()
	cur.execute("SELECT * FROM Category")
	return cur.fetchall()

def insert_user(db_conn, user_obj):
    cur = db_conn.cursor()
    try:
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
        
def get_users(db_conn):
	cur = db_conn.cursor()
	cur.execute("SELECT * FROM User")
	return cur.fetchall()

def insert_product(db_conn, product_obj):
    cur = db_conn.cursor()
    try:
        cur.execute(
			f"""
			INSERT INTO Product
			(
				product_name, product_details, price, quantity, category_id
			)
			VALUES (
				'{product_obj['product_name']}',
				'{product_obj['product_details']}',
				{product_obj['price']},
				{product_obj['quantity']},
				{product_obj['category_id']}
			)
			""")
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)
        
def get_products(db_conn):
	cur = db_conn.cursor()
	cur.execute("SELECT * FROM Product")
	return cur.fetchall()

def insert_order(db_conn, order_obj):
    cur = db_conn.cursor()
    try:
        cur.execute(f"""
			INSERT INTO Order_Table
			(
				user_id, shipping_address, city, country
			)
			VALUES (
				{order_obj["user_id"]},
				'{order_obj["shipping_address"]}',
				'{order_obj["city"]}',
				'{order_obj["country"]}'
			);
		""")
        db_conn.commit()
        cur.execute("SELECT LAST_INSERT_ID() AS id;")
        return cur.fetchall()[0]['id']
    except pymysql.Error as e:
        print('Something went wrong,', e)

def insert_order_details(db_conn, order_details_list):
    cur = db_conn.cursor()
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

def insert_payment(db_conn, payment_obj):
    cur = db_conn.cursor()
    try:
        cur.execute(f"""
			INSERT INTO Payment
			(
				total_amount, order_id
			)
			VALUES (
				{payment_obj["total_amount"]},
				{payment_obj["order_id"]}
			);
		""")
        db_conn.commit()
        cur.execute("SELECT LAST_INSERT_ID() AS id;")
        return cur.fetchall()[0]['id']
    except pymysql.Error as e:
        print('Something went wrong,', e)
        
def update_total_amount_and_payment_id_in_order(db_conn, order_id, total_amount, payment_id):
    cur = db_conn.cursor()
    try:
        cur.execute(f"""
			UPDATE Order_Table
   			SET total_amount = {total_amount}, payment_id = {payment_id}
			WHERE id = {order_id};
		""")
        db_conn.commit()
    except pymysql.Error as e:
        print('Something went wrong,', e)

def get_orders_by_user_id(db_conn, user_id):
	cur = db_conn.cursor()
	try:
		cur.execute(f"SELECT * FROM Order_Table WHERE user_id = {user_id}")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong,', e)

def get_order_details_by_order_id(db_conn, order_id):
	cur = db_conn.cursor()
	try:
		cur.execute(f"SELECT * FROM Order_Details WHERE order_id = {order_id}")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong,', e)

def get_products_by_id(db_conn, product_ids):
	cur = db_conn.cursor()
	try:
		cur.execute(f"SELECT * FROM Product WHERE id IN {product_ids}")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong,', e)
  
def get_products_by_order_id_and_user_id(db_conn, order_id, user_id):
    print('user_id =', user_id)
    print('order_id =', order_id)
    cur = db_conn.cursor()
    try:
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
  
def add_product_by_name(db_conn, product_name, cat_id):
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
 
def update_product_name_by_id(db_conn, product_name, product_id):
	cur = db_conn.cursor()
	cur.execute(
		f"""
		UPDATE product 
  		SET name = '{product_name}'
    	WHERE id = {product_id};
		""")
	db_conn.commit()
 
def delete_product_by_id(db_conn, product_id):
    cur = db_conn.cursor()
    cur.execute(f"DELETE FROM product WHERE id = {product_id}")
    db_conn.commit()

def get_products(db_conn):
	cur = db_conn.cursor()
	cur.execute("SELECT * FROM product")
	return cur.fetchall()

def get_categories_and_products(db_conn):
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