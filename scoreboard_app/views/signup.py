import time
import flet as ft
import db.user_crud as user_crud
import db.db as db

class Signup(ft.UserControl):
    def __init__(self, page: ft.Page):
        self.page = page
        super().__init__()
        

        self.username_field = ft.TextField(hint_text="Username")
        self.password_field = ft.TextField(hint_text="Password", password=True, can_reveal_password=True)
        self.confirm_password_field = ft.TextField(hint_text="Confirm Password", password=True)
        self.error_field = ft.Text(value='',color = ft.colors.RED_500)
        self.signup_button = ft.ElevatedButton("Sign Up", on_click=self.on_signup_click)

    def build(self):
        return ft.SafeArea(
 
            content= ft.Column(
            controls=[
                self.username_field,
                self.password_field,
                self.confirm_password_field,
                self.error_field,
                self.signup_button,
                ft.TextButton("Already have an account? Log in here",on_click=lambda e: self.page.go("/login")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        )

    def on_signup_click(self, event):
        username = self.username_field.value
        password = self.password_field.value
        confirm_password = self.confirm_password_field.value

        conn = db.connect()
        if not conn:
            self.error_field.value = "Database connection error"
            self.update()
            return
        if user_crud.check_data_exists(conn,f"username='{username}'"):
            print("User already exists!")
            self.error_field.value = "User already exists!"
            self.update()
        elif password != confirm_password:
            print("Passwords do not match!")
            self.error_field.value = "Passwords do not match!"
            self.update()
        else:
            user_crud.create_user(conn,username, password)
            self.page.splash = ft.ProgressBar()
            self.error_field.value = "User created successfully!"
            self.error_field.color = ft.colors.GREEN
            time.sleep(2)
            self.page.splash = None

            self.page.go("/login")