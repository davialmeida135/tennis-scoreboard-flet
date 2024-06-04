import flet as ft

class Signup(ft.UserControl):
    def __init__(self):
        super().__init__()
        

        self.username_field = ft.TextField(hint_text="Username")
        self.password_field = ft.TextField(hint_text="Password", password=True, can_reveal_password=True)
        self.confirm_password_field = ft.TextField(hint_text="Confirm Password", password=True)
        self.signup_button = ft.ElevatedButton("Sign Up", on_click=self.on_signup_click)

    def build(self):
        return ft.SafeArea(
 
            content= ft.Column(
            controls=[
                self.username_field,
                self.password_field,
                self.confirm_password_field,
                self.signup_button,
                ft.TextButton("Already have an account? Log in here"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        )

    def on_signup_click(self, event):
        username = self.username_field.value
        password = self.password_field.value
        confirm_password = self.confirm_password_field.value

        if password != confirm_password:
            print("Passwords do not match!")
        else:
            # Here you can call the function to create a user in your database
            # For example: create_user(conn, username, password)
            print(f"User {username} signed up with password {password}")