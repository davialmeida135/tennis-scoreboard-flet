from flet import  ListView, Page, UserControl
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
        
        
        # Create a ListView with some items
        
    def build(self):
        return ListView(
                controls=[
                self.texto,
                ft.Text(value="Item 1"),
                ft.Text(value="Item 2"),
                ft.Text(value="Item 3"),
                ft.ElevatedButton("Go to settings", on_click=lambda e: self.page.go("/match")),
                ],
                
            )


    def on_item_click(self, item):
        print(f"You clicked on {item['text']}")