from flet import ListView, Page, UserControl, TextField, ElevatedButton, Text, Column
import flet as ft

class Menu(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
        self.texto = ft.Text(value="Nenhum usuario")
        if page is not None:
            logged_in = self.page.session.get("logged_user")
            if logged_in:
                self.texto.value = f"Usuario logado: {logged_in['username']}"
        
        self.stream_id_field = ft.TextField(hint_text="Enter Stream ID or Link")

    def build(self):
        return ListView(
            controls=[
                self.texto,
                ft.ElevatedButton("Login", on_click=lambda e: self.page.go("/login")),
                ft.ElevatedButton("Register", on_click=lambda e: self.page.go("/signup")),
                Column(
                    controls=[
                        self.stream_id_field,
                        ft.ElevatedButton("Watch Stream", on_click=self.watch_stream)
                    ]
                )
            ],
        )

    def watch_stream(self, e):
        stream_id_or_link = self.stream_id_field.value
        if stream_id_or_link:
            # Assuming the stream URL is constructed using the stream ID or link
            stream_url = f"http://192.168.1.107:8551/scoreboard_app/main.py/stream/{stream_id_or_link}"
            self.page.overlay.clear()
            self.page.overlay.append(
                ft.Container(
                    content=ft.Text(stream_url),
                    padding=5,
                    width=self.page.width / 2,
                    height=self.page.height / 2,
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.symmetric(horizontal=self.page.width / 4, vertical=self.page.height / 6),
                    shadow=ft.BoxShadow(
                        spread_radius=0.5,
                        blur_radius=5,
                        color=ft.colors.BLACK,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.NORMAL,
                    ),
                )
            )
            self.page.update()