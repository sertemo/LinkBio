import reflex as rx
from datetime import datetime
import LinkBio.styles.styles as styles
from LinkBio.styles.styles import Color, TextColor


def footer() -> rx.Component:
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.image(
                src='favicon.ico',
                html_width='40px',
                html_height='auto'
                ),
            rx.chakra.text(
            'Hecho con Reflex',
            font_size=styles.Size.MEDIUM.value,
            margin_bottom=styles.Size.ZERO.value
            ),
            rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.text(
                        f'© 2022-{datetime.today().year} sertemo',
                        font_size=styles.Size.MEDIUM.value),
                    href='https://github.com/sertemo',
                    is_external=True),
                margin_top=styles.Size.ZERO.value
            ),                
            rx.chakra.text(
                'BUILDING YOUR IDEAS',
                font_size=styles.Size.MEDIUM.value,
                margin_top=styles.Size.ZERO.value
                ),
            margin_bottom=styles.Size.BIG.value,
            color=TextColor.FOOTER.value,
            padding_bottom=styles.Size.BIG.value
        ),
        margin_top=styles.Size.BIG.value
    )