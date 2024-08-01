import flet as ft
class StreamInput(ft.Column):
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

        self.stream_input_field = ft.TextField(hint_text="Match Id or URL",filled=True ,bgcolor = ft.colors.WHITE,expand=True, color=ft.colors.BLACK )
 
        def clear_overlay(e):
            self.page.overlay.clear()
            self.page.update()
        
        def go_stream(e):
            try:
                page.go(f'/stream/{int(self.stream_input_field.value)}')
            except:
                page.go(self.stream_input_field.value)
            finally:
                clear_overlay(e)
            


        self.close_button = ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.WHITE, alignment=ft.alignment.center_right,on_click=clear_overlay)
        self.submit_button = ft.IconButton(icon=ft.icons.CHECK, icon_color=ft.colors.WHITE, alignment=ft.alignment.center_right,on_click=go_stream,tooltip="Submit")

        self.controls = [
                ft.Row(
                    controls=[self.stream_input_field,self.submit_button,self.close_button,
                    ]
                ),       
        ]