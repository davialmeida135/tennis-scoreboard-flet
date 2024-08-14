import sqlite3
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, '../db.db')
def get_user_credentials():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT username, password FROM user WHERE TRUE LIMIT 1")
    result = c.fetchone()
    conn.close()
    print("RETORNANDO CREDENCIAIS DO USUARIO -----------------")
    return result

# Function to save user credentials to the database
def save_user_credentials(username, password):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO user (id, username, password) VALUES (1, ?, ?)", (username, password))
    conn.commit()
    conn.close()
    print("SALVANDO CREDENCIAIS DO USUARIO -------------------------")

# Function to delete user credentials from the database
def delete_user_credentials():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM user WHERE TRUE")
    conn.commit()
    conn.close()
