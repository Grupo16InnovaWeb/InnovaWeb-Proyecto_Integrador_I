from db import get_connection
from datetime import datetime
import hashlib

# --- Encriptar password (simple hash sha256) ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Crear usuario ---
def create_user(username, email, password, role="user"):
    conn = get_connection()
    cur = conn.cursor()
    hashed = hash_password(password)
    sql = "INSERT INTO users (username, email, password_hash, role) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (username, email, hashed, role))
    conn.commit()
    cur.close()
    conn.close()
    return True

# --- Buscar usuario por username o email ---
def get_user_by_username_or_email(value):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    sql = "SELECT * FROM users WHERE username = %s OR email = %s"
    cur.execute(sql, (value, value))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

# --- Verificar login ---
def authenticate_user(username_or_email, password):
    user = get_user_by_username_or_email(username_or_email)
    if not user:
        return None
    if user["password_hash"] == hash_password(password):
        return user
    return None

# --- Actualizar perfil ---
def update_user_profile(user_id, username=None, email=None, password=None):
    conn = get_connection()
    cur = conn.cursor()
    fields, values = [], []
    if username:
        fields.append("username=%s")
        values.append(username)
    if email:
        fields.append("email=%s")
        values.append(email)
    if password:
        fields.append("password_hash=%s")
        values.append(hash_password(password))
    if not fields:
        return False
    values.append(user_id)
    sql = f"UPDATE users SET {', '.join(fields)}, updated_at=%s WHERE id=%s"
    values.insert(-1, datetime.now())
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    conn.close()
    return True


# --- Listar todos los usuarios ---
def list_users():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

# --- Cambiar rol de usuario ---
def change_role(user_id, new_role):
    if new_role not in ["user", "admin"]:
        raise ValueError("Rol inválido")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET role=%s, updated_at=%s WHERE id=%s", (new_role, datetime.now(), user_id))
    conn.commit()
    cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

# --- Eliminar usuario ---
def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return True


def get_user_by_username_or_email(value):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    sql = "SELECT * FROM users WHERE username = %s OR email = %s"
    cur.execute(sql, (value, value))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user
