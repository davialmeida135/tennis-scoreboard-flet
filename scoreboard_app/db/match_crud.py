def get_data(conn, conditions=None):
    cursor = conn.cursor()
    if conditions:
        cursor.execute(f"SELECT * FROM match WHERE {conditions}")
    else:
        cursor.execute(f"SELECT * FROM match")

    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    result = [{columns[i]:row[i] for i in range(len(columns))} for row in rows]
    return result

def check_data_exists(conn,condition):
    cursor = conn.cursor()
    cursor.execute(f"SELECT EXISTS (SELECT 1 FROM match WHERE {condition})")
    return cursor.fetchone()[0]==1

def create_match(conn, owner_id, match_info):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO match (owner_id, match_info) VALUES (?, ?)", (owner_id, match_info)
    )
    conn.commit()

def update_match(conn, match_id, match_info):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE match SET match_info = ? WHERE id = ?", (match_info, match_id)
    )
    conn.commit()

def delete_match(conn, match_id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM match WHERE id = ?", (match_id,)
    )
    conn.commit()