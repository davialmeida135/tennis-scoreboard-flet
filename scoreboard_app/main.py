import flet as ft
from views.scoreboard import Scoreboard
from views.tennismatch import TennisMatch
from views.menu import Menu
from views.signup import Signup
from views.login import Login
from views.matches import Matches
from service.match_service import *
from views.new_match_overlay import NewMatch

def main(page: ft.Page):

    print("initial route:", page.route)

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        
        troute = ft.TemplateRoute(e.route)
        page.views.append(
            ft.View(
            "/",
            [
                Menu(page),
                ft.ElevatedButton("Sign-up", on_click=open_signup),
                ft.ElevatedButton("Log-in", on_click=open_login),
            ],
            )
        )

        if troute.match("/match/:id"):
            match_id = troute.id
            match = get_match(match_id)
            page.views.append(
                ft.View(
                route = f"/match/{match_id}",
                controls= 
                [
                    Scoreboard(match,page),
                ],
                bottom_appbar=ft.BottomAppBar(
                    bgcolor=ft.colors.GREEN,
                    shape=ft.NotchShape.CIRCULAR,
                    content=ft.Row(
                        controls=[ft.Container(expand=True), ft.IconButton(icon=ft.icons.LOGOUT, icon_color=ft.colors.WHITE, on_click=open_matches)],
                    ),
                ),
                bgcolor = ft.colors.DEEP_ORANGE,
            )
        )
        elif e.route == '/matches':
            page.views.clear()
            user_id=page.session.get("logged_user")['id']
            user_matches = get_player_matches(user_id)   
            #user_matches = get_player_matches('1')  
            page.views.append(
                ft.View(
                route ="/matches",
                controls= 
                [
                    Matches(page, user_matches),
                ],
              
                bottom_appbar=ft.BottomAppBar(
                    bgcolor=ft.colors.GREEN,
                    shape=ft.NotchShape.CIRCULAR,
                    content=ft.Row(
                        controls=[
                            ft.Container(expand=True),   
                            ft.IconButton(icon=ft.icons.LOGOUT, icon_color=ft.colors.WHITE, on_click=logout),
                        ]
                    ),
                ),
                floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, 
                                                                 bgcolor = ft.colors.GREEN_800, 
                                                                 on_click= open_create_match),
                floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED,
                bgcolor = ft.colors.DEEP_ORANGE,
            )
        )      
        elif e.route =="/matches/new":
            page.go("/matches")
        elif e.route == '/signup':
            print("Signup changed")
            page.views.append(
                ft.View(
                route ="/signup",
                controls=
                [
                    Signup(page),
                    
                ],
                bgcolor="grey",
            )
            )
        
        elif e.route == '/login':
            print("Login changed")
            page.views.append(
                ft.View(
                route ="/login",
                controls=
                [
                    Login(page),
                    
                ],
                bgcolor="grey",
            )
            )
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    #menu = Menu()
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_matches(e):
        page.go("/matches")

    def open_signup(e):
        page.go("/signup")

    def open_login(e):
        page.go("/login")

    def logout(e):
        page.session.clear()
        open_login(e)

    def open_create_match(e):
        print(page.width)
        print(page.height)

        if page.width > page.height:
            margem = ft.margin.symmetric(horizontal=page.width/4, vertical=page.height/6)
            relative_width = page.width/2
            relative_height = page.height/2
        else:
            margem = ft.margin.symmetric(horizontal=page.width/10, vertical=page.height/6)
            relative_width = page.width/1.2
            relative_height = page.height/2
    
        page.overlay.append(
            ft.Container(
                content=NewMatch(page),
                padding=5,
                width=relative_width,
                height=relative_height,
                bgcolor=ft.colors.GREEN_800,
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
        page.update()
        #time.sleep(5)
        #page.overlay.clear()
        #page.update()
   
    page.go('/login')

ft.app(main)
