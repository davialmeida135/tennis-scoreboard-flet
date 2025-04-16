import flet as ft
import config
from model.user import User
from views.stream_input_overlay import StreamInput
from views.stream_url_overlay import StreamUrl
from views.scoreboard import Scoreboard
from views.signup import Signup
from views.login import Login
from views.matches import Matches
import service.match_service as match_service
from service import user_service
from views.new_match_overlay import NewMatch
from views.scoreboard_stream import ScoreboardStream
import db.user_storage as user_storage

def main(page: ft.Page):
    #print("initial route:", page.route)

    def route_change(e):
        #print("Route change:", e.route)
        page.views.clear()
        
        troute = ft.TemplateRoute(e.route)
        
        if troute.match("/match/:id"):
            # Check if user is logged in
            if page.session.contains_key("logged_user"):
                match_id = troute.id
                #print('match: '+ str(match_id))
                logged_user = User(logged_user=page.session.get("logged_user"))
                #print('player matches: '+str(get_player_matches_id(logged_user)))
                
                if int(match_id) in match_service.get_player_matches_id(logged_user):
                    match = match_service.get_match(match_id)
                    page.views.append(
                        ft.View(
                        route = f"/match/{match_id}",
                        controls= 
                        [
                            Scoreboard(match, page),
                        ],
                        bottom_appbar=ft.BottomAppBar(
                            bgcolor=config.BOTTOM_BAR,
                            shape=ft.NotchShape.CIRCULAR,
                            content=ft.Row(
                            controls=[
                                ft.Container(expand=True),
                                ft.IconButton(icon=ft.icons.SHARE, icon_color=ft.colors.WHITE, on_click=lambda e: share_overlay(e,match_id)) ,
                                ft.IconButton(icon=ft.icons.LOGOUT, icon_color=ft.colors.WHITE, on_click=open_matches)
                                ],
                        ),
                        ),
                        bgcolor = config.APP_BG,
                    )
                    )
                else:
                    page.go("/matches")
            else:
                page.go("/")

        elif troute.match("/stream/:id"):
            page.views.clear()
            match_id = troute.id
            match = match_service.get_match(match_id)
            page.views.append(
                ft.View(
                route = f"/stream/{match_id}",
                controls= 
                [
                    ScoreboardStream(match, page),
                ],
                bottom_appbar=ft.BottomAppBar(
                    bgcolor=config.BOTTOM_BAR,
                    shape=ft.NotchShape.CIRCULAR,
                    content=ft.Row(
                        controls=[
                            ft.Container(expand=True),
                            ft.IconButton(icon=ft.icons.REMOVE_RED_EYE_OUTLINED, icon_color=ft.colors.WHITE, on_click=stream_overlay),
                            ft.IconButton(icon=ft.icons.SHARE, icon_color=ft.colors.WHITE, on_click=lambda e: share_overlay(e,match_id)) ,
                            ft.IconButton(icon=ft.icons.LOGOUT, icon_color=ft.colors.WHITE, on_click=open_matches)
                            ],
                    ),
                ),
                bgcolor = config.APP_BG,
            )
            )

        elif e.route == '/matches':
            
            # Check if user is logged in
            if page.session.contains_key("logged_user"):
                logged_user = User(logged_user=page.session.get("logged_user"))
                user_matches = match_service.get_player_matches(logged_user)   
                page.views.append(
                    ft.View(
                    route ="/matches",
                    controls= 
                    [
                        Matches(page, user_matches),
                    ],
                  
                    bottom_appbar=ft.BottomAppBar(
                        bgcolor=config.BOTTOM_BAR,
                        shape=ft.NotchShape.CIRCULAR,
                        content=ft.Row(
                            controls=[
                                ft.Container(expand=True),
                                ft.IconButton(icon=ft.icons.REMOVE_RED_EYE_OUTLINED, icon_color=ft.colors.WHITE, on_click=stream_overlay),
                                ft.IconButton(icon=ft.icons.LOGOUT, icon_color=ft.colors.WHITE, on_click=logout),
                            ]
                        ),
                    ),
                    floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, 
                                                                    bgcolor = config.MAIN_COLOR_1, 
                                                                    on_click= open_create_match),
                    floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED,
                    bgcolor = config.APP_BG,
                )
            )
            else:
                page.go("/")
        elif e.route =="/matches/new":
            page.go("/matches")
        elif e.route == '/signup':
            #print("Signup changed")
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
            #print("Login changed")
            page.go("/")
        elif e.route == '/':
            page.views.append(
            ft.View(
                "/",
                controls=[
                    Login(page),
                    
                ],
                bottom_appbar=ft.BottomAppBar(
                        bgcolor=config.BOTTOM_BAR,
                        shape=ft.NotchShape.CIRCULAR,
                        content=ft.Row(
                            controls=[
                                ft.Container(expand=True),
                                
                                ft.IconButton(icon=ft.icons.REMOVE_RED_EYE_OUTLINED, icon_color=ft.colors.WHITE, on_click=stream_overlay)
                                ],
                        ),
                    ),
                    bgcolor = config.APP_BG,
                ),
            
            )
        page.update()

    def view_pop(e):
        #print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def stream_overlay(e):
    
        if page.width > page.height:
            margem = ft.margin.symmetric(horizontal=page.width/4, vertical=page.height/6)
            relative_width = page.width/2
            relative_height = page.height/8
        else:
            margem = ft.margin.symmetric(horizontal=page.width/10, vertical=page.height/6)
            relative_width = page.width/1.2
            relative_height = page.height/7

        page.overlay.clear()
        page.overlay.append(
            ft.Container(
                content=StreamInput(page),
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
        page.update()

    def open_matches(e):
        page.go("/matches")

    def open_signup(e):
        page.go("/signup")

    def open_login(e):
        page.go("/")

    def logout(e):
        page.session.clear()
        try:
            user_storage.delete_user_credentials(page)
            print("Credentials removed from storage.")
        except Exception:
            print("No credentials found in storage.")
        open_login(e)
    
    def share_overlay(e,id):
        if page.width > page.height:
            margem = ft.margin.symmetric(horizontal=page.width/4, vertical=page.height/6)
            relative_width = page.width/2
            relative_height = page.height/8
        else:
            margem = ft.margin.symmetric(horizontal=page.width/10, vertical=page.height/6)
            relative_width = page.width/1.2
            relative_height = page.height/7

        url = "https://tennis.digi.com.br/stream/"+str(id)

        page.overlay.clear()
        page.overlay.append(
            ft.Container(
                content=StreamUrl(page,url),
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
        page.update()
        
    def open_create_match(e):
        #print(page.width)
        #print(page.height)

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
        page.update()

    def on_app_start(page):
        creds = user_storage.get_user_credentials(page)
        if creds:
            try:
                user = user_service.authenticate(creds[0], creds[1])
                page.session.set("logged_user", {"username": creds[0], "access_token": user.access_token, "refresh_token": user.refresh_token})
                page.go("/matches")
            except (Exception, ValueError) as e:
                print(f"Error during auto-login: {e}")
                page.go("/")
        else:
            page.go("/")
        

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    on_app_start(page)

ft.app(main)