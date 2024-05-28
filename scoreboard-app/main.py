import flet as ft
from scoreboard import Scoreboard
from tennismatch import TennisMatch


def main(page: ft.Page):

    match = TennisMatch('Davi','Gustavo')
    match.start_match()
    
    board = Scoreboard(match)

    page.add(board)
    
ft.app(main)



