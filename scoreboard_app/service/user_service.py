import sqlite3
from db import user_crud
import bcrypt
from db import db
from model.user import User

def hash_password(password):
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def create_user(username, password):
    conn = db.connect()
    """Create a new user with a hashed password."""
    hashed_password = hash_password(password)
    user_crud.create_user(conn, username, hashed_password)

def authenticate(username, password):
    conn = db.connect()
    """Authenticate a user."""
    # Retrieve the stored hashed password from the database
    stored_hashed_password = user_crud.get_user_password(conn, username)
    if stored_hashed_password:
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
            id = user_crud.get_user_id(conn, username)
            user = User(id,username)
            return user
        raise ValueError("Invalid password")
    raise ValueError("Invalid username")
    
    

def get_user_id(username):
    conn = db.connect()
    return user_crud.get_user_id(conn, username)

def validate_user(username, password, confirm_password):
    """Validate user input."""
    if not username or not password or not confirm_password:
        raise ValueError("Please fill in all fields")
    if password != confirm_password:
        raise ValueError("Passwords do not match")
    if len(password) < 5:
        raise ValueError("Password must be at least 8 characters long")
    if len(username) < 4:
        raise ValueError("Username must be at least 4 characters long")
    return None

def delete_user(username, password):
    conn = db.connect()
    """Delete a user."""
    try:
        authenticate(username, password)
    
        user_crud.delete_user(conn, username)
        return True
    except ValueError as e:
        return False
    