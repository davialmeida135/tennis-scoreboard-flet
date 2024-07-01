import flet as ft
import sys
import os
from views.edit_overlay import Edit
from model.tennismatch import TennisMatch
import service.match_service as match_service
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config


class MatchCard(ft.Card):
    def __init__(self, match : TennisMatch,  page: ft.Page,):
        super().__init__()
        #Variables
        self.match = match
        self.page=page
        self.placar_1 = []
        self.placar_2 = []

        #Flet objects/config

        self.color = ft.colors.GREEN
        self.elevation = ft.colors.BLACK
        self.shape = ft.RoundedRectangleBorder(radius=5)
        

    def build_placar_1(self):
        self.placar_1 = []
        
        self.placar_1.append(
            ft.Container(
                content=ft.Text(value=self.match.player1, color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                alignment=ft.alignment.center,
                
                padding=5,
                height=50,
                width=90,
                gradient=ft.RadialGradient(
                    center=ft.alignment.bottom_right,
                    colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                    radius=1,
                ),
                border_radius=ft.border_radius.all(5),
            ),
        )

        #Sets finalizados
        for set in self.match.match_moment.sets:
            self.placar_1.append(
                ft.Container(
                    content=ft.Text(value=set.player1_score, color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2, text_align=ft.TextAlign.CENTER),
                    alignment=ft.alignment.center,
                    padding=5,
                    height=50,
                    width=30,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[config.MAIN_COLOR_2,config.MAIN_COLOR_1,],
                        
                    ),
                    border_radius=ft.border_radius.all(5),
                )
            )
        #Set em andamento
        self.placar_1.append(
            ft.Container(
                        content=ft.Text(value=self.match.match_moment.current_set.player1_score, color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                        alignment=ft.alignment.center,
                        padding=10,
                        height=50,
                        width=31,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[config.CURRENT_SET_COLOR_1,config.CURRENT_SET_COLOR_2,],
                            
                        ),
                        border_radius=ft.border_radius.all(5),
                    )
        )

        #Game em andamento
        self.placar_1.append(
            ft.Container(
                content=ft.Text(
                    value=self.match.match_moment.current_game.player1_score,
                    color=ft.colors.GREY_800,
                    weight=ft.FontWeight.BOLD,
                    width=100,
                    max_lines=2,
                    text_align=ft.TextAlign.CENTER,
                    ),
                alignment=ft.alignment.center,
                width=51.6,
                height=50,
                #bgcolor=ft.colors.WHITE,
                border_radius=ft.border_radius.all(5),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[config.CURRENT_GAME_COLOR_1,config.CURRENT_GAME_COLOR_2,],
                ),
            )
        )
        
    def build_placar_2(self):
        self.placar_2 = []
        
        self.placar_2.append(
            ft.Container(
                content=ft.Text(value=self.match.player2, color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                alignment=ft.alignment.center,
                
                padding=5,
                height=50,
                width=90,
                gradient=ft.RadialGradient(
                    center=ft.alignment.bottom_right,
                    colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                    radius=1,
                ),
                border_radius=ft.border_radius.all(5),
            ),
        )

        #Sets finalizados
        for set in self.match.match_moment.sets:
            self.placar_2.append(
                ft.Container(
                    content=ft.Text(value=set.player2_score, color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2, text_align=ft.TextAlign.CENTER),
                    alignment=ft.alignment.center,
                    padding=5,
                    height=50,
                    width=30,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[config.MAIN_COLOR_2,config.MAIN_COLOR_1,],
                        
                    ),
                    border_radius=ft.border_radius.all(5),
                )
            )
        #Set em andamento
        self.placar_2.append(
            ft.Container(
                        content=ft.Text(value=self.match.match_moment.current_set.player2_score, color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                        alignment=ft.alignment.center,
                        padding=10,
                        height=50,
                        width=31,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[config.CURRENT_SET_COLOR_1,config.CURRENT_SET_COLOR_2,],
                            
                        ),
                        border_radius=ft.border_radius.all(5),
                    )
        )

        #Game em andamento
        self.placar_2.append(
            ft.Container(
                content=ft.Text(
                    value=self.match.match_moment.current_game.player2_score,
                    color=ft.colors.GREY_800,
                    weight=ft.FontWeight.BOLD,
                    width=100,
                    max_lines=2,
                    text_align=ft.TextAlign.CENTER,
                    ),
                alignment=ft.alignment.center,
                width=51.6,
                height=50,
                #bgcolor=ft.colors.WHITE,
                border_radius=ft.border_radius.all(5),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[config.CURRENT_GAME_COLOR_1,config.CURRENT_GAME_COLOR_2,],
                ),
            )
        )
        
    def build(self):
        self.build_placar_1()
        self.build_placar_2()
        
        self.content=ft.Container(
                content=ft.Column(
                    spacing=0,
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.SPORTS_TENNIS, color=ft.colors.YELLOW),
                            title=ft.Text(self.match.title, weight= ft.FontWeight.BOLD),
                            trailing=ft.Column(controls=[
                                ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit),
                            ],
                            ),
                            on_click=self.view_match,
                        ),
                        
                        ft.Row(
                            #Player 1
                            spacing = 0,
                            alignment=ft.MainAxisAlignment.START,
                            controls = self.placar_1
                            
                        ),
                        ft.Row(
                            #Player 2
                            spacing = 0,
                            alignment=ft.MainAxisAlignment.START,
                            controls=self.placar_2
                        ),

                    ]
                    
                ),
                width=400,
                padding=10,
                
                
                #bgcolor=ft.colors.GREY,
            )
        #self.content = self.coluna

    def view_match(self, b):
        self.page.go(f"/match/{self.match.match_id}")
        print("View", self.match)




    def edit(self, b):
        if self.page.width > self.page.height:
            margem = ft.margin.symmetric(horizontal=self.page.width/4, vertical=self.page.height/6)
            relative_width = self.page.width/2
            relative_height = self.page.height/7
        else:
            margem = ft.margin.symmetric(horizontal=self.page.width/10, vertical=self.page.height/6)
            relative_width = self.page.width/1.2
            relative_height = self.page.height/7

        self.page.overlay.clear()
        self.page.overlay.append(
            ft.Container(
                content=Edit(self.page,self.match),
                padding=5,
                width=relative_width,
                height=relative_height,
                bgcolor=config.MAIN_COLOR_1,
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.all(10),
                margin=margem,
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
        print("Edit", self.match)
        #self.page.splash()
        



class MatchList(ft.ListView):
    def __init__(self, page: ft.Page, match_list):
        super().__init__()
        self.page = page
        self.match_list = match_list
        self.adaptive=True
        
        for match in match_list:
            self.controls.append(MatchCard(match,page))
        #if page.session.contains_key("logged_user"):
            #self.user_display.value = page.session.get("logged_user")["id"]

class Matches(ft.Column):
    def __init__(self, page: ft.Page, match_list):
        super().__init__()
        self.match_list=match_list
        self.page = page
        #self.height = page.height-50
        self.user_display = ft.Text("Usuario legal")
        self.expand=True

    def build(self):
        return ft.SafeArea( 
            MatchList(self.page,self.match_list),
            expand=True              
        )
