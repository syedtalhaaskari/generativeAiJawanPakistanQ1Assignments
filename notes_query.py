import pymysql
import db

def insert_category(name):
	try:
		db_conn = db.mysqlconnect()
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
		db.disconnect()
  
def get_categories():
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM Category ORDER BY name")
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()
  
def get_category_by_id(id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute("SELECT * FROM Category WHERE id = %(id)s", {
			"id": id
		})
        return cur.fetchone()
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
		db.disconnect()

def get_user(username):
	try:
		db_conn = db.mysqlconnect()
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
		db.disconnect()

def get_user_by_id(user_id):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(
			f"""
			Select * FROM User
			WHERE id = %(user_id)s
			""", { 
				'user_id' : user_id
			})
		return cur.fetchone()
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		db.disconnect()

def get_session_by_id(session_obj):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(
			f"""
			Select * FROM User_session
			WHERE session_id = %(session_id)s AND ip_address = %(ip_address)s
			""", { 
				'session_id' : session_obj["session_id"],
				'ip_address' : session_obj["ip_address"]
			})
		return cur.fetchone()
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		db.disconnect()
  
def insert_session(session_obj):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute(
			f"""
			INSERT INTO User_session 
			(
				session_id,
				user_id,
				ip_address
			)
			VALUES (
				%(session_id)s,
				%(user_id)s,
				%(ip_address)s
			)
			""", {
				'session_id' : session_obj['session_id'],
				'user_id' : session_obj['user_id'],
				'ip_address' : session_obj['ip_address']
			})
		db_conn.commit()
		return True
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		db.disconnect()
  
def get_user_notes(user_id, title = None, category_id = None, date_created = None):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        query_str = "SELECT * FROM Note WHERE user_id = %(user_id)s"
        if title is not None:
            query_str += " AND title LIKE %(title)s"
        if category_id is not None:
            query_str += " AND category_id = %(category_id)s"
        if date_created is not None:
            query_str += " AND date_created = %(date_created)s"
        cur.execute(query_str, {
			"user_id" : user_id,
			"title" : "%" + title if title is not None else '' + "%",
			"category_id" : category_id,
			"date_created" : date_created
		})
        return cur.fetchall()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()
  
def get_note_by_id(user_id, note_id):
    try:
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()
        cur.execute(f"SELECT * FROM Note WHERE user_id = %(user_id)s AND id = %(id)s;", {
			"user_id" : user_id,
			"id" : note_id,
		})
        print('4')
        return cur.fetchone()
    except pymysql.Error as e:
        print('Something went wrong,', e)
    finally:
        db.disconnect()

def insert_note(note_obj):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute("""
			INSERT INTO Note 
			(
				user_id,
				title,
				content,
				category_id
			)
			VALUES (
				%(user_id)s,
				%(title)s,
				%(content)s,
				%(category_id)s
			)
		""", { 
				'user_id' : note_obj['user_id'],
				'title' : note_obj['title'],
				'content' : note_obj['content'],
				'category_id' : note_obj['category_id']
		})
		db_conn.commit()
		return True
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		db.disconnect()

def update_note(note_obj):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute("""
			UPDATE Note 
			SET 
				title = %(title)s,
				content = %(content)s,
                category_id = %(category_id)s
			WHERE user_id = %(user_id)s AND id = %(note_id)s
		""", { 
			'user_id' : note_obj['user_id'],
			'note_id' : note_obj['note_id'],
			'title' : note_obj['title'],
			'content' : note_obj['content'],
			'category_id' : note_obj['category_id']
		})
		db_conn.commit()
		return True
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		db.disconnect()

def delete_note(user_id, note_id):
	try:
		db_conn = db.mysqlconnect()
		cur = db_conn.cursor()
		cur.execute("""
			DELETE FROM Note
			WHERE user_id = %(user_id)s AND id = %(note_id)s
		""", { 
			'user_id' : user_id,
			'note_id' : note_id
		})
		db_conn.commit()
		return True
	except pymysql.Error as e:
		print('Something went wrong,', e)
		return e
	finally:
		db.disconnect()