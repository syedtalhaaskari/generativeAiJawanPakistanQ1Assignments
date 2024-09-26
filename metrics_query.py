import pymysql

import db

def get_total_revenue():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
				CONCAT('$', d.today_revenue) AS "Today Revenue",
				CONCAT('$', w.this_week_revenue) AS "This Week's Revenue",
				CONCAT('$', m.this_month_revenue) AS "This Month's Revenue"
			FROM (
				SELECT SUM(total_amount) AS today_revenue
				FROM order_table 
				WHERE delivery_date > DATE_SUB(NOW(), INTERVAL 1 DAY)
			) d
			JOIN (
				SELECT SUM(total_amount) AS this_week_revenue
				FROM order_table 
				WHERE delivery_date > DATE_SUB(NOW(), INTERVAL 1 WEEK)
			) w
			JOIN (
				SELECT SUM(total_amount) AS this_month_revenue
				FROM order_table 
				WHERE delivery_date > DATE_SUB(NOW(), INTERVAL 1 MONTH)
			) m;
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_revenue_by_city(start_date = None, end_date = None):
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		if start_date is not None and end_date is not None:
			cur.execute("""
				SELECT
					city,
					CONCAT('$', SUM(total_amount)) AS total_revenue
				FROM order_table
				WHERE order_status = 'Delivered' AND delivery_date >= %(start_date)s AND delivery_date <= %(end_date)s
				GROUP BY city;
			""", {
				'start_date': start_date,
                'end_date': end_date
			})
		elif start_date is not None:
			cur.execute("""
				SELECT
					city,
					CONCAT('$', SUM(total_amount)) AS total_revenue
				FROM order_table
				WHERE order_status = 'Delivered' AND delivery_date >= %(start_date)s
				GROUP BY city;
			""", {
				'start_date': start_date
			})
		elif start_date is not None:
			cur.execute("""
				SELECT
					city,
					CONCAT('$', SUM(total_amount)) AS total_revenue
				FROM order_table
				WHERE order_status = 'Delivered' AND delivery_date <= %(end_date)s
				GROUP BY city;
			""", {
				'end_date': end_date
			})
		else:
			cur.execute("""
				SELECT
					city,
					CONCAT('$', SUM(total_amount)) AS total_revenue
				FROM order_table
				WHERE order_status = 'Delivered'
				GROUP BY city;
			""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_revenue_by_product(start_date = None, end_date = None):
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		if start_date is not None and end_date is not None:
			cur.execute("""
				SELECT
					p.product_name,
					CONCAT('$', SUM(od.total_price)) AS total_revenue
				FROM order_table o
				JOIN order_details od
					ON o.id = od.order_id
				JOIN product p
					ON p.id = od.product_id
				WHERE o.order_status = 'Delivered' AND o.delivery_date >= %(start_date)s AND o.delivery_date <= %(end_date)s
				GROUP BY p.id;
			""", {
				'start_date': start_date,
                'end_date': end_date
			})
		elif start_date is not None:
			cur.execute("""
				SELECT
					p.product_name,
					CONCAT('$', SUM(od.total_price)) AS total_revenue
				FROM order_table o
				JOIN order_details od
					ON o.id = od.order_id
				JOIN product p
					ON p.id = od.product_id
				WHERE o.order_status = 'Delivered' AND o.delivery_date >= %(start_date)s
				GROUP BY p.id;
			""", {
					'start_date': start_date
				})
		elif end_date is not None:
			cur.execute("""
				SELECT
					p.product_name,
					CONCAT('$', SUM(od.total_price)) AS total_revenue
				FROM order_table o
				JOIN order_details od
					ON o.id = od.order_id
				JOIN product p
					ON p.id = od.product_id
				WHERE o.order_status = 'Delivered' AND o.delivery_date <= %(end_date)s
				GROUP BY p.id;
			""", {
				'end_date': end_date
			})
		else:
			cur.execute("""
				SELECT
					p.product_name,
					CONCAT('$', SUM(od.total_price)) AS total_revenue
				FROM order_table o
				JOIN order_details od
					ON o.id = od.order_id
				JOIN product p
					ON p.id = od.product_id
				WHERE o.order_status = 'Delivered'
				GROUP BY p.id;
			""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_this_month_top_selling_products():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
				p.id,
				p.product_name,
				SUM(od.quantity) AS total_units
			FROM order_table o
			JOIN order_details od
				ON o.id = od.order_id
			JOIN product p
				ON p.id = od.product_id
			WHERE order_status = 'Delivered' AND delivery_date > DATE_SUB(NOW(), INTERVAL 1 MONTH)
			GROUP BY p.id
			ORDER BY SUM(od.quantity) DESC;
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_order_metrics():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
				(
					SELECT
						COUNT(o.id)
					FROM order_table o
					WHERE order_date > DATE_SUB(NOW(), INTERVAL 1 MONTH)
				) AS 'Total Orders This Month',
				(
					SELECT
						COUNT(o.id)
					FROM order_table o
					WHERE o.order_status = 'Cancelled'    
				) AS 'Total Cancelled Orders',
				(
					SELECT
						COUNT(o.id)
					FROM order_table o
					WHERE o.order_status = 'Payment Pending'
				) AS 'Total Pending Orders',
				(
					SELECT
						COUNT(o.id)
					FROM order_table o
					WHERE o.order_status = 'Delivered'
				) AS 'Total Successful Orders';
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_payment_metrics():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
				(
					SELECT
						CONCAT('$', SUM(p.total_amount))
					FROM payment p
					JOIN order_table o
						ON p.order_id = o.id
					WHERE o.order_date > DATE_SUB(NOW(), INTERVAL 1 MONTH) AND p.payment_status = 'Pending'
				) AS 'Pending Payments (This Month)',
				(
					SELECT
						CONCAT('$', SUM(p.total_amount))
					FROM payment p
					JOIN order_table o
						ON p.order_id = o.id
					WHERE o.order_date > DATE_SUB(NOW(), INTERVAL 1 MONTH) AND p.payment_status = 'Paid'
				) AS 'Successful Payments (This Month)';
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_payment_metrics():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
				(
					SELECT
						CONCAT('$', SUM(p.total_amount))
					FROM payment p
					JOIN order_table o
						ON p.order_id = o.id
					WHERE o.order_date > DATE_SUB(NOW(), INTERVAL 1 MONTH) AND p.payment_status = 'Pending'
				) AS 'Pending Payments (This Month)',
				(
					SELECT
						CONCAT('$', SUM(p.total_amount))
					FROM payment p
					JOIN order_table o
						ON p.order_id = o.id
					WHERE o.order_date > DATE_SUB(NOW(), INTERVAL 1 MONTH) AND p.payment_status = 'Paid'
				) AS 'Successful Payments (This Month)';
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_inventory_levels():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
			  	id,
			  	product_name,
				quantity
			FROM Product;
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_out_of_stock_products():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
			  	id,
			  	product_name,
				quantity
			FROM Product
			WHERE quantity = 0;
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_top_cities_by_sales():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
			  	city,
			  	COUNT(id) AS 'Total Orders'
			FROM Order_Table
			WHERE order_status = 'Delivered' AND delivery_date > DATE_SUB(NOW(), INTERVAL 1 MONTH)
			GROUP BY city
			ORDER BY 'Total Orders' desc;
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()

def get_top_countries_by_sales():
	db_conn = db.mysqlconnect()
	cur = db_conn.cursor()
	try:
		cur.execute("""
			SELECT
			  	country,
			  	CONCAT('$', SUM(total_amount)) AS 'Total Revenue'
			FROM Order_Table
			WHERE order_status = 'Delivered' AND delivery_date > DATE_SUB(NOW(), INTERVAL 1 MONTH)
			GROUP BY country
			ORDER BY 'Total Revenue' desc;
		""")
		return cur.fetchall()
	except pymysql.Error as e:
		print('Something went wrong:', e)
	finally:
		db.disconnect()