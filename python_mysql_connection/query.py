def add_category_by_name(db_conn, category_name):
	cur = db_conn.cursor()
	cur.execute(
		f"""
		INSERT INTO category 
		(
			name
		)
		VALUES (
			'{category_name}'
		)
		""")
	db_conn.commit()
  
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

def get_categories(db_conn):
	cur = db_conn.cursor()
	cur.execute("SELECT * FROM category")
	return cur.fetchall()

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