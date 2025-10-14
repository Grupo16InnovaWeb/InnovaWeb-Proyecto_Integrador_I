# db.py
import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"        # o 'innoweb_user' si lo creaste
DB_PASSWORD = ""        # contraseña de root en XAMPP
DB_NAME = "innoweb"

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
