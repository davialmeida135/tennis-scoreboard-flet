import flet as ft
from views.scoreboard import Scoreboard
from tennismatch import TennisMatch
from views.menu import Menu
from views.signup import Signup

from router import views_handler


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
                Menu(),
                ft.ElevatedButton("Go to settings", on_click=open_match),
                ft.ElevatedButton("Sign-up", on_click=open_signup),
            ],
        )
        )

        if troute.match("/match/:id"):
            print("Match:", troute.id)
            
        elif e.route == '/match':
            print("Match changed")
            #page.views.clear()
            match = TennisMatch('Davi','Gustavo')
            match.start_match()
            page.views.append(
                ft.View(
                route ="/match",
                controls=
                [
                    Scoreboard(match),
                    ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ],
                bgcolor="grey",
            )
            )
            
        elif e.route == '/signup':
            print("Signup changed")
            page.views.append(
                ft.View(
                route ="/signup",
                controls=
                [
                    Signup(),
                    ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
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

    def open_match(e):
        page.go("/match")

    def open_signup(e):
        page.go("/signup")

    
    page.go('/')

    


ft.app(main)
