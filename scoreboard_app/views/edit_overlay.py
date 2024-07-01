import flet as ft
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import service.match_service as match_service
from model.tennismatch import TennisMatch


class Edit(ft.Column):
    def __init__(self, page: ft.Page, match: TennisMatch):
        super().__init__()
        self.page=page
        self.match=match

        if self.page.width > self.page.height:
                self.margem = ft.margin.symmetric(horizontal=self.page.width/4, vertical=self.page.height/6)
                self.relative_width = self.page.width/2
                self.relative_height = self.page.height/2
        else:
            self.margem = ft.margin.symmetric(horizontal=self.page.width/10, vertical=self.page.height/6)
            self.relative_width = self.page.width/1.2
            self.relative_height = self.page.height/2

        self.match_name_field = ft.TextField(value= match.title,filled=True ,bgcolor = ft.colors.WHITE,expand=True, color=ft.colors.BLACK )
 
        def clear_overlay(e):
            self.page.overlay.clear()
            self.page.update()
        
        def edit_match(e):
            self.match.title = self.match_name_field.value
            match_service.update_match(self.match.match_id, self.match)
            self.page.overlay.clear()
            self.page.update()
            page.go("/matches/new")


        self.close_button = ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.WHITE, alignment=ft.alignment.center_right,on_click=clear_overlay)
        self.submit_button = ft.IconButton(icon=ft.icons.CHECK_CIRCLE_ROUNDED, icon_color=ft.colors.WHITE, alignment=ft.alignment.center_right,on_click=edit_match)

        self.controls = [
                ft.Row(
                    controls=[self.match_name_field,self.submit_button,self.close_button,
                    ]
                ),       
        ]
       