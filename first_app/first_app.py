"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .components.navbar import navbar


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),

    )

def about():
    # About Page
    return rx.container(
        rx.text('About Page')
    )



app = rx.App()
app.add_page(index)
app.add_page(about, route='/about')
app.add_page(navbar)