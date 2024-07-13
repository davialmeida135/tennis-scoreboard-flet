import sqlite3
from db import user_crud
import bcrypt
from db import db
from model.user import User
import os

def save_tokens(access_token, refresh_token):
    os.environ['TENNIS_ACCESS_TOKEN'] = access_token
    os.environ['TENNIS_REFRESH_TOKEN'] = refresh_token

def load_tokens():
    access_token = os.environ.get('TENNIS_ACCESS_TOKEN')
    refresh_token = os.environ.get('TENNIS_REFRESH_TOKEN')
    return access_token, refresh_token

def hash_password(password):
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def create_user(username, password):
    
    """Create a new user with a hashed password."""
    hashed_password = hash_password(password)
    try:
        user_crud.create_user(username.lower(), hashed_password)
    except Exception as e:
        raise e

def authenticate(username, password):
    
    """Authenticate a user."""
    # Retrieve the stored hashed password from the database
    auth_response = user_crud.auth_user(username.lower(), password)
    if auth_response:
        user = User(username,auth_response['access_token'],auth_response['refresh_token'])
        save_tokens(auth_response['access_token'],auth_response['refresh_token'])
        return user
    else:
        raise ValueError("Invalid username or password")
    

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

    """Delete a user."""
    try:
        authenticate(username, password)
    
        user_crud.delete_user( username)
        return True
    except ValueError as e:
        return False
    