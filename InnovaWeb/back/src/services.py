from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from models import User
from db import SessionLocal

def create_user(username: str, email: str, password: str, role: str = "user"):
    session = SessionLocal()
    try:
        # check uniqueness
        exists = session.query(User).filter(or_(User.username == username, User.email == email)).first()
        if exists:
            session.close()
            raise ValueError("Username o email ya existente.")
        user = User(username=username, email=email, role=role)
        user.set_password(password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except IntegrityError as e:
        session.rollback()
        raise
    finally:
        session.close()

def authenticate_user(username_or_email: str, password: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter(
            or_(User.username == username_or_email, User.email == username_or_email)
        ).first()
        if user and user.verify_password(password):
            return user
        return None
    finally:
        session.close()

def get_user_by_id(user_id: int):
    session = SessionLocal()
    try:
        return session.query(User).get(user_id)
    finally:
        session.close()

def get_user_by_username(username: str):
    session = SessionLocal()
    try:
        return session.query(User).filter_by(username=username).first()
    finally:
        session.close()

def list_users():
    session = SessionLocal()
    try:
        return session.query(User).order_by(User.id).all()
    finally:
        session.close()

def change_role(user_id: int, new_role: str):
    session = SessionLocal()
    try:
        user = session.query(User).get(user_id)
        if not user:
            raise ValueError("Usuario no existe")
        user.role = new_role
        session.commit()
        session.refresh(user)
        return user
    finally:
        session.close()

def delete_user(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).get(user_id)
        if not user:
            raise ValueError("Usuario no existe")
        session.delete(user)
        session.commit()
        return True
    finally:
        session.close()

def update_user_profile(user_id: int, username: str = None, email: str = None, password: str = None):
    session = SessionLocal()
    try:
        user = session.query(User).get(user_id)
        if not user:
            raise ValueError("Usuario no existe")
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.set_password(password)
        session.commit()
        session.refresh(user)
        return user
    finally:
        session.close()
