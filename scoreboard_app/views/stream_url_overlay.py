import flet as ft
class StreamUrl(ft.Column):
    def __init__(self, page: ft.Page, stream_url: str):
        super().__init__()
        self.page=page
        self.stream_url = stream_url

        if self.page.width > self.page.height:
                self.margem = ft.margin.symmetric(horizontal=self.page.width/4, vertical=self.page.height/6)
                self.relative_width = self.page.width/2
                self.relative_height = self.page.height/2
        else:
            self.margem = ft.margin.symmetric(horizontal=self.page.width/10, vertical=self.page.height/6)
            self.relative_width = self.page.width/1.2
            self.relative_height = self.page.height/2

        self.stream_url_field = ft.TextField(read_only=True,value= self.stream_url,filled=True ,bgcolor = ft.colors.WHITE,expand=True, color=ft.colors.BLACK )
 
        def clear_overlay(e):
            self.page.overlay.clear()
            self.page.update()
        
        def copy_stream_url(e):
            self.page.set_clipboard(self.stream_url)
            
            


        self.close_button = ft.IconButton(icon=ft.icons.CLOSE, icon_color=ft.colors.WHITE, alignment=ft.alignment.center_right,on_click=clear_overlay)
        self.copy_button = ft.IconButton(icon=ft.icons.COPY, icon_color=ft.colors.WHITE, alignment=ft.alignment.center_right,on_click=copy_stream_url,tooltip="Copy to clipboard")

        self.controls = [
                ft.Row(
                    controls=[self.stream_url_field,self.copy_button,self.close_button,
                    ]
                ),       
        ]