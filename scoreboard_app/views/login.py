import flet as ft
import db.user_crud as user_crud
import db.db as db
import time

class Login(ft.UserControl):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.error_field = ft.Text(value='',color = ft.colors.RED_500)
        self.username_field = ft.TextField(hint_text="Username")
        self.password_field = ft.TextField(hint_text="Password", password=True, can_reveal_password=True)

        self.login_button = ft.ElevatedButton("Login", on_click=self.login)

        
    def build(self):
        return ft.SafeArea(
 
            content= ft.Column(
            controls=[
                self.error_field,
                self.username_field,
                self.password_field,
                self.login_button,
                ft.TextButton("Don't have an account? Register in here", on_click=lambda e: self.page.go("/signup")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        )

    def login(self,b):
        username = self.username_field.value
        password = self.password_field.value

        conn = db.connect()
        if not conn:
            self.error_field.value = "Database connection error"
            self.update()
            return
        if not (username and password):
            self.error_field.value = "Please enter username and password"
            self.update()
            return
        if user_crud.check_data_exists(conn,f"username = '{username}'"):
            get_user = user_crud.get_data(conn, f"username = '{username}'")
            
            username_check = get_user['username'] == username
            password_check = get_user['password'] == password

            if username_check and password_check:
                self.page.session.clear()
                self.page.session.set("logged_user", {"id": get_user['id'], "username": get_user['username']})
                self.page.go("/matches",)
