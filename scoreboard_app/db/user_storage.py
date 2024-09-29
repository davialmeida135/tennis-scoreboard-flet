import sqlite3
import os
import flet as ft
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, '../db.db')
'''def get_user_credentials():
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
'''
#Get user credentials from the page client storage
def get_user_credentials(page: ft.Page):
    usr = page.client_storage.get("current_usr")
    pwd = page.client_storage.get("current_pwd")
    return usr, pwd

#Save user credentials to the page client storage
def save_user_credentials(page: ft.Page, username, password):
    page.client_storage.set("current_usr", username)
    page.client_storage.set("current_pwd", password)

#Delete user credentials from the page client storage
def delete_user_credentials(page: ft.Page):
    page.client_storage.delete("current_usr")
    page.client_storage.delete("current_pwd")

