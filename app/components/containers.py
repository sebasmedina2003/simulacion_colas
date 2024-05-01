import flet as ft

class ContainerSimulation(ft.Container):
    def __init__(self):
        super().__init__(content=ft.Text("This is Tab 2"), alignment=ft.alignment.center)
        self.content = ft.Text("This is Tab 2")


class ContainerSettings(ft.Container):
    def __init__(self):
        super().__init__(content=ft.Text("This is Tab 2"), alignment=ft.alignment.center)
        self.content = ft.Text("This is Tab 1")