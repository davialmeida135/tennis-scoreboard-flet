import flet as ft
from views.menu import Menu
from views.scoreboard import Scoreboard
from tennismatch import TennisMatch

def views_handler(page, route):
    return {
        "/":ft.View(
            route = "/", 
            controls = [
                Menu(page)
            ]
        ),
        "/match": ft.View(
            route = "/match",
            controls = [
                
            ]
        )
    }

def route_match(page : ft.Page,match : TennisMatch, route = '/match' ):
    return

