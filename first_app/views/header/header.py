import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.text(
            "header test", 
            height="40px"
        ),
        position = "sticky",
        bg = "blue",
        padding = "10px",
    )