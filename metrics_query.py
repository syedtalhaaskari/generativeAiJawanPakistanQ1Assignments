import pymysql

def get_categories(db_conn):
	cur = db_conn.cursor()
	cur.execute("SELECT * FROM Category")
	return cur.fetchall()