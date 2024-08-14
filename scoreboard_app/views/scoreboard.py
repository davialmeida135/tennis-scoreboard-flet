from typing import Any
import flet as ft
import sys,os
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    TextField
    )
import config
from service import user_service
from views.stream_url_overlay import StreamUrl

from model.tennismatch import TennisMatch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from service.match_service import update_match

class Scoreboard(UserControl):
    def __init__(self, match: TennisMatch, page: ft.Page):
        super().__init__()
        self.match = match
        self.page = page
        self.placar_1 = Row(
            spacing=0,
        )
        self.placar_2 = Row(
            spacing=0,
        )

    def update_placar_1(self):
        self.placar_1.controls.clear()
        #Nome do jogador
        self.placar_1.controls.append(
            ft.Container(
                content=ft.Text(size=config.SCOREBOARD_PLAYER_SIZE,value=self.match.player1, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                alignment=ft.alignment.center,
                
                padding=5,
                height=50,
                width=90,
                gradient=ft.RadialGradient(
                    center=ft.alignment.bottom_right,
                    colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                    radius=1,
                ),
                #border_radius=ft.border_radius.all(5),
            ),
        )

        #Sets finalizados
        for set in self.match.match_moment.sets:
            self.placar_1.controls.append(
                ft.Container(
                    content=ft.Text(value=set.player1_score, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2,size=config.SCOREBOARD_TEXT_SIZE),
                    alignment=ft.alignment.center,
                    padding=5,
                    height=50,
                    width=30,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[config.MAIN_COLOR_2,config.MAIN_COLOR_1,],
                        
                    ),
                    #border_radius=ft.border_radius.all(5),
                )
            )
        #Set em andamento
        self.placar_1.controls.append(
            ft.Container(
                        content=ft.Text(value=self.match.match_moment.current_set.player1_score, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2,size=config.SCOREBOARD_TEXT_SIZE),
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
        self.placar_1.controls.append(
            ft.Container(
                content=ft.Text(
                    value=self.match.match_moment.current_game.player1_score,
                    color=colors.GREY_800,
                    weight=ft.FontWeight.BOLD,
                    width=100,
                    max_lines=2,
                    text_align=ft.TextAlign.CENTER,
                    size=config.SCOREBOARD_TEXT_SIZE,
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

    def update_placar_2(self):
        self.placar_2.controls.clear()
        #Nome do jogador
        self.placar_2.controls.append(
            ft.Container(
                content=ft.Text(size=config.SCOREBOARD_PLAYER_SIZE,value=self.match.player2, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2),
                alignment=ft.alignment.center,
                
                padding=5,
                height=50,
                width=90,
                gradient=ft.RadialGradient(
                    center=ft.alignment.bottom_right,
                    colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                    radius=1,
                ),
                #border_radius=ft.border_radius.all(5),
            ),
        )

        #Sets finalizados
        for set in self.match.match_moment.sets:
            self.placar_2.controls.append(
                ft.Container(
                    content=ft.Text(value=set.player2_score, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2,size=config.SCOREBOARD_TEXT_SIZE),
                    alignment=ft.alignment.center,
                    padding=5,
                    height=50,
                    width=30,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[config.MAIN_COLOR_2,config.MAIN_COLOR_1,],
                        
                    ),
                    #border_radius=ft.border_radius.all(5),
                )
            )

        #Set em andamento
        self.placar_2.controls.append(
            ft.Container(
                content=ft.Text(value=self.match.match_moment.current_set.player2_score, color=colors.WHITE,weight=ft.FontWeight.BOLD,width=90,max_lines=2,size=config.SCOREBOARD_TEXT_SIZE),
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
        self.placar_2.controls.append(
            ft.Container(
                content=ft.Text(
                    value=self.match.match_moment.current_game.player2_score,
                    color=colors.GREY_800,
                    weight=ft.FontWeight.BOLD,
                    width=100,
                    max_lines=2,
                    text_align=ft.TextAlign.CENTER,
                    size=config.SCOREBOARD_TEXT_SIZE,
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
        
    ## Criacao do placar
        self.update_placar_1()
        self.update_placar_2()


    ## Texto dos botões grandes de pontuação
        self.botao_1 = ft.Text(value=self.match.match_moment.current_game.player1_score, size=50, color=colors.WHITE)
        self.botao_2 = ft.Text(value=self.match.match_moment.current_game.player2_score, size=50, color=colors.WHITE)       
        
        self.page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor = config.MAIN_COLOR_1)
        self.page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
        self.page.bottom_appbar = ft.BottomAppBar(
            bgcolor=config.BOTTOM_BAR,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    
                    ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
                ]
            ),
        )    
        return ft.SafeArea(
 
            content= 
            Container(
                        #width=300,
                        #height=450,
                        bgcolor=config.APP_BG,
                        #border_radius=border_radius.all(5),
                        padding=4,
                        content=Column(
                            spacing=50,
                            controls=[
                                Row(
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    controls = [
                                        
                                        ft.Icon(name=ft.icons.SPORTS_BASEBALL_ROUNDED, color=ft.colors.YELLOW),
                                        ft.Text("Tennis Scoreboard",
                                            size=20,
                                            color=ft.colors.WHITE,
                                            #bgcolor=ft.colors.GREEN_700,
                                            weight=ft.FontWeight.BOLD,
                                            #italic=True,
                                            ),
                                        ft.Icon(name=ft.icons.SPORTS_BASEBALL_ROUNDED, color=ft.colors.YELLOW)
                                        ]
                                ),
                                
#======================================== NOMES JOGADORES ===================================
                                Row(
                                    controls=[
                                        Container(
                                            width=150,
                                            height=60,
                                            expand=True,
                                            border_radius=border_radius.all(5),
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_center,
                                                end=ft.alignment.bottom_center,
                                                colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                                            ),  
                                            content=Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    Text(
                                                        value=self.match.player1,
                                                        color=colors.WHITE,
                                                        weight=ft.FontWeight.BOLD,
                                                        size=15,
                                                        width=140,
                                                        max_lines=2,
                                                        text_align=ft.TextAlign.CENTER),
                                                ],
                                                
                                            ),
                                             
                                        ),
                                        Container(
                                            width=150,
                                            height=60,
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_center,
                                                end=ft.alignment.bottom_center,
                                                colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                                            ),
                                            border_radius=border_radius.all(5),
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        value=self.match.player2,
                                                        color=colors.WHITE,
                                                        weight=ft.FontWeight.BOLD,
                                                        size=15,
                                                        width=140,
                                                        max_lines=2,
                                                        text_align=ft.TextAlign.CENTER),
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            expand=True,
                                        )
                                    ]
                                ),
#==================================== BOTÕES DE PONTUAÇÃO ===================================
                                Row(
                                    controls=[
                                        Container(
                                            expand=1,
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_center,
                                                end=ft.alignment.bottom_center,
                                                colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                                            ),
                                            border_radius=border_radius.all(10),
                                            content=ft.FilledButton(
                                            #width=142,
                                            height=142,
                                            on_click = self.point_player1,
                                            
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                bgcolor=ft.colors.BLACK12,
                                                
                                            ),
                                            content=ft.Container(
                                            # bgcolor=ft.colors.GREEN_ACCENT_400,
                                                
                                                content=ft.Column(controls=
                                                    [
                                                        self.botao_1,
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                )
                                                
                                            ),
                                            expand=True,
                                        )),
                                        Container(
                                            expand=1,
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_center,
                                                end=ft.alignment.bottom_center,
                                                colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                                            ),
                                            border_radius=border_radius.all(10),
                                            content=ft.FilledButton(
                                                #width=142,
                                                height=142,
                                                on_click = self.point_player2,
                                                
                                                style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(radius=10),
                                                    bgcolor=ft.colors.BLACK12,
                                                                                                  ),
                                                content=ft.Container(
                                                    content=ft.Column(controls=
                                                    [
                                                        self.botao_2,
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                )                                            
                                                ),
                                                expand=True,
                                            ))
                                    ]
                                ),
#==================================== UNDO // REDO ===================================
                                Row(
                                    controls=[
                                        Container(
                                            expand=1,
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_center,
                                                end=ft.alignment.bottom_center,
                                                colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                                            ),
                                            border_radius=border_radius.all(10),
                                            content=ft.FilledButton(
                                                
                                                on_click = self.undo_pressed,
                                                style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(radius=10),
                                                    bgcolor=ft.colors.with_opacity(0, '#ff6666'),
                                                ),
                                                content=ft.Container(
                                                # bgcolor=ft.colors.GREEN_ACCENT_400,
                                                    
                                                    content=ft.Row(
                                                        controls=[ 
                                                        
                                                        ft.Icon(name=ft.icons.UNDO_ROUNDED, color=ft.colors.WHITE,size=30),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                    ),
                                                    
                                                ),
                                                expand=True,
                                            )
                                        ),
                                        Container(
                                            expand=1,
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_center,
                                                end=ft.alignment.bottom_center,
                                                colors=[config.MAIN_COLOR_1,config.MAIN_COLOR_2],
                                            ),
                                            border_radius=border_radius.all(10),
                                            content=ft.FilledButton(
                                                
                                                on_click = self.redo_pressed,
                                                style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(radius=10),
                                                    bgcolor=ft.colors.with_opacity(0, '#ff6666'),
                                                ),
                                                content=ft.Container(
                                                # bgcolor=ft.colors.GREEN_ACCENT_400,
                                                    
                                                    content=ft.Row(
                                                        controls=[ 
                                                        
                                                        ft.Icon(name=ft.icons.REDO_ROUNDED, color=ft.colors.WHITE,size=30),
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                    ),
                                                    
                                                ),
                                                expand=True,
                                            )
                                        )
                                    ]
                                ),
#================================== PLACAR =======================================                              
                                Row(
                                    controls=[
                                        Container(
                                            expand=1,
                                            bgcolor=colors.GREEN_800,
                                            border_radius=border_radius.all(5),
                                            #height=100,
                                            content = Column(
                                                spacing =0,
                                                controls = [
                                                    self.placar_1,
                                                    self.placar_2,
                                                ],
                                            ),
                                        )
                                    ]
                                ),
#================================
                                
                            ],
                        ),
                    ),
            )
        

    
    def update_all(self):
        self.botao_1.value = self.match.match_moment.current_game.player1_score  
        self.botao_2.value = self.match.match_moment.current_game.player2_score 
        self.update_placar_1()
        self.update_placar_2()
        
        update_match(self.match)
        topic_name = "match_topic_"+str(self.match.match_id)
        self.page.pubsub.send_all_on_topic(topic_name,self.match)
        self.update()

    def point_player1(self, button):
        self.match.point(self.match.player1)

        #atualizar bd

        self.update_all()
      
    def point_player2(self, button):
        self.match.point(self.match.player2)

        #atualizar bd

        self.update_all()

    def undo_pressed(self, button):
        ##print("Undo")
        self.match.undo()
        self.update_all()
   
    def redo_pressed(self, button):
        ##print("redo")
        self.match.redo()
        self.update_all()
