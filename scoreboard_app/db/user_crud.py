import sqlite3
import db

def get_data(conn, conditions=None):
    cursor = conn.cursor()
    if conditions:
        cursor.execute(f"SELECT * FROM user WHERE {conditions}")
    else:
        cursor.execute(f"SELECT * FROM user")

    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    print(columns)

    result = {columns[i]: row[i] for row in rows for i in range(len(columns))}
    #print(result)
    return result

def check_data_exists(conn,condition):
    cursor = conn.cursor()
    cursor.execute(f"SELECT EXISTS (SELECT 1 FROM user WHERE {condition})")
    return cursor.fetchone()[0]==1

def create_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)", (username, password)
    )
    conn.commit()

def update_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE user SET password = ? WHERE username = ?", (password, username)
    )
    conn.commit()

def delete_user(conn, username):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM user WHERE username = ?", (username,)
    )
    conn.commit()

def get_user_password(conn, username):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM user WHERE username = ? LIMIT 1", (username,)
    )
    return cursor.fetchone()[0]

def authenticate(conn, username, password):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM user WHERE username = ? AND password = ? LIMIT 1", (username, password)
    )
    return cursor.fetchone() is not None

def get_user_id(conn, username):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM user WHERE username = ? LIMIT 1", (username,)
    )
    return cursor.fetchone()[0]

