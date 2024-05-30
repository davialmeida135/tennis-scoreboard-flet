import sqlite3
def connect(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def get_data(conn, table_name, conditions=None):
    cursor = conn.cursor()
    if conditions:
        cursor.execute(f"SELECT * FROM {table_name} WHERE {conditions}")
    else:
        cursor.execute(f"SELECT * FROM {table_name}")

    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    result = [{columns[i]:row[i]} for i in range(len(columns)) for row in rows]

def check_data_exists(conn,table_name,condition):
    cursor = conn.cursor()
    cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {table_name} WHERE {condition})")
    return cursor.fetchone()[0]==1


def create_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)", (username, password)
    )
    conn.commit()

