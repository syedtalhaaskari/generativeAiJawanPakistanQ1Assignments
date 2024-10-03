import os
from dotenv import load_dotenv
import pymysql

load_dotenv()

DB_HOST = os.getenv('DB_HOST') or 'localhost'
DB_PORT = int(os.getenv('DB_PORT') or '3306') 
DB_USER = os.getenv('DB_USER') or 'root'
DB_PASSWORD = os.getenv('DB_PASSWORD') or ''
DB_DBNAME = os.getenv('DB_DBNAME') or 'Notes'

db_conn = {}

def mysqlconnect():
    global db_conn
    # To connect MySQL database
    db_conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_DBNAME,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return db_conn

def disconnect():
    db_conn.close()