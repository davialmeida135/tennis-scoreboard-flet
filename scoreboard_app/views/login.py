import flet as ft
import db.user_crud as user_crud
import time
from service import user_service
import config
import db.user_storage as user_storage
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

        try:
            user = user_service.authenticate(username, password)
            self.page.session.clear()
            self.page.session.set("logged_user", {"username": username,"access_token": user.access_token, "refresh_token": user.refresh_token})            
            
            user_storage.save_user_credentials(self.page,username,password)
        
            self.page.go("/matches")
        except (Exception,ValueError) as e:
            self.error_field.value = str(e)
            self.update()
            return
