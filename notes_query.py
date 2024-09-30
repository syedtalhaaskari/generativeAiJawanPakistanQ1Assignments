import pymysql
import notes_db

def insert_category(name):
	try:
		db_conn = notes_db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(
			f"""
			INSERT INTO Category 
			(
				name
			)
			VALUES (
				%(name)s
			)
			""", { 'name' : name })
		db_conn.commit()
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		notes_db.disconnect()
  
def get_categories():
    try:
        db_conn = notes_db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM Category ORDER BY name")
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        notes_db.disconnect()

def insert_user(user_obj):
	try:
		db_conn = notes_db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(
			f"""
			INSERT INTO User 
			(
				username,
				password
			)
			VALUES (
				%(username)s,
				%(password)s
			)
			""", { 
				'username' : user_obj['username'],
				'password' : user_obj['password']
			})
		db_conn.commit()
		return True
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		notes_db.disconnect()

def get_user(username):
	try:
		db_conn = notes_db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(
			f"""
			Select * FROM User
			WHERE username = %(username)s
			""", { 
				'username' : username
			})
		return cur.fetchone()
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		notes_db.disconnect()