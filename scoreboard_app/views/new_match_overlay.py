import flet as ft
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import service.match_service as match_service
from model.tennismatch import TennisMatch
from service import user_service

class NewMatch(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page=page

        if self.page.width > self.page.height:
                self.margem = ft.margin.symmetric(horizontal=self.page.width/4, vertical=self.page.height/6)
                self.relative_width = self.page.width/2
                self.relative_height = self.page.height/2
        else:
            self.margem = ft.margin.symmetric(horizontal=self.page.width/10, vertical=self.page.height/6)
            self.relative_width = self.page.width/1.2
            self.relative_height = self.page.height/2
        self.player1_name_field = ft.TextField(label="Player 1 Name",filled=True ,bgcolor = ft.colors.WHITE,expand=True, color=ft.colors.BLACK )
        self.player2_name_field = ft.TextField(label="Player 2 Name",filled=True ,bgcolor = ft.colors.WHITE,expand=True, color=ft.colors.BLACK)

        self.max_sets_dropdown = ft.Dropdown(
            label="Max Sets",
            options=[ft.dropdown.Option(text="3", key=3),
                    ft.dropdown.Option(text="5", key=5),
                    ],
            bgcolor=ft.colors.WHITE,
            expand=True,
            
        )    

        self.match_tiebreak_dropdown = ft.Dropdown(
            label="Match Tiebreak",
            options=[ft.dropdown.Option(text="No", key=False),
                    ft.dropdown.Option(text="Yes", key=True)],
            bgcolor=ft.colors.WHITE,
            alignment=ft.alignment.center,
            expand=True,
            
        )
        def create_match(e):
            #print("Create match clicked")
            player1_name = self.player1_name_field.value
            player2_name = self.player2_name_field.value
            max_sets = self.max_sets_dropdown.value
            match_tiebreak = self.match_tiebreak_dropdown.value
            match = TennisMatch(player1=player1_name, player2=player2_name, match_id=None)
            match.start_match()
            
            match_service.add_match(match, )
            self.page.overlay.clear()
            self.page.go("/matches/new")
        
        def clear_overlay(e):
            self.page.overlay.clear()
            self.page.update()

        self.create_match_button = ft.ElevatedButton(text="START", on_click=create_match)

        self.close_button = ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.WHITE, alignment=ft.alignment.center_right,on_click=clear_overlay)

        self.controls = [
                ft.Row(controls=[
                    ft.Text("START A NEW MATCH", size=20, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    ft.Container(expand=True),
                        self.close_button
                        ],
                    ),
                ft.Row(
                    controls=[self.player1_name_field,
                        self.player2_name_field,]
                ),
                ft.Row(
                    controls=[self.max_sets_dropdown,
                        self.match_tiebreak_dropdown,]
                ),                        
                ft.Row(
                    controls=[self.create_match_button,],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.END
                ), 
                
        ]
       


