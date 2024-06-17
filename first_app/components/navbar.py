import reflex as rx


# def navbar() -> rx.Component:
#     return rx.hstack(
#         rx.text(
#             "navbar test", 
#             height="40px"
#         ),
#         position = "sticky",
#         bg = "blue",
#         padding = "10px",
#     )


def navbar() -> rx.Component:
    return rx.flex(
        rx.badge(
            rx.icon(tag="table-2", size=28),
            rx.heading("Customer Data App", size="6"),
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.spacer(),
        rx.hstack(
            rx.logo(),
            rx.color_mode.button(),
            align="center",
            spacing="3",
        ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
        padding_top="2em",
    )