"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .components.navbar import navbar
from .views.header.header import header
from .components.form_field import form_field
from .backend.backend import State
from .views.main import add_collection

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        navbar(),
        header(),
        rx.box(
            add_collection(),
        ),  
    )

app = rx.App()
app.add_page(index)
app.add_page(navbar)
app._compile() # Compile the app 