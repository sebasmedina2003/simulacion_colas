from constants.interface import *
from components.containers import *
import time
import flet as ft


def main(page: ft.Page):
    page.title = "Colas de trabajo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                icon=ft.icons.SETTINGS,
                text="Settings",
                content=ContainerSettings(),
            ),
            ft.Tab(
                icon=ft.icons.PLAY_ARROW,
                text="Simulation",
                content=ContainerSimulation(),
            ),
        ],
        expand=1,
    )

    page.add(t)


if __name__ == "__main__":
    ft.app(target=main)
