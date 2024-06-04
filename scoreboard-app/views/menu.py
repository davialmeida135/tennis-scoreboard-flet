from flet import  ListView, Page, UserControl
import flet as ft


class Menu(ft.UserControl):
    def __init__(self):
        super().__init__()
        

        # Create a ListView with some items
        
    def build(self):
        return ListView(
                controls=[
                ft.Text(value="Item 1"),
                ft.Text(value="Item 2"),
                ft.Text(value="Item 3"),
                ft.ElevatedButton("Go to settings", on_click=lambda e: self.page.go("/match")),
                ],
                
            )


    def on_item_click(self, item):
        print(f"You clicked on {item['text']}")