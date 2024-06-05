import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_name = "db.db"

db_path = os.path.join(BASE_DIR, db_name)

def connect():
    return sqlite3.connect(db_path)

def table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", {table_name})
    return cursor.fetchone() is not None

def create_database():
    conn = sqlite3.connect(db_path)

    if os.path.exists(db_path):
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
            """
        )

        cursor.execute(
            """
            CREATE TABLE match (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_id INTEGER ,
                match_info TEXT NOT NULL,
                FOREIGN KEY (
                owner_id
            )
                REFERENCES user (id) ON DELETE CASCADE
            );
            """
            )

