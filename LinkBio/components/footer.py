import reflex as rx
from datetime import datetime


def footer() -> rx.Component:
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.image(
                src='img/stm_logo.png',
                html_width='100px',
                html_height='auto'
                ),
                rx.chakra.hstack(
                    rx.chakra.link(
                        rx.chakra.text(f'© 2022-{datetime.today().year} sertemo'),
                        href='https://github.com/sertemo',
                        is_external=True),
                    rx.chakra.text('BUILDING YOUR IDEAS')
                ),                
        ),
        bg='lightblue'
    )