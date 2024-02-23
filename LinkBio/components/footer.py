import reflex as rx
from datetime import datetime
import LinkBio.styles.styles as styles


def footer() -> rx.Component:
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.image(
                src='img/stm_logo.png',
                html_width='70px',
                html_height='auto'
                ),
            rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.text(
                        f'© 2022-{datetime.today().year} sertemo',
                        font_size=styles.Size.MEDIUM.value),
                    href='https://github.com/sertemo',
                    is_external=True),
            ),                
            rx.chakra.text(
                'BUILDING YOUR IDEAS',
                font_size=styles.Size.MEDIUM.value,
                margin_top='0px !important'
                ),
            margin_bottom=styles.Size.BIG.value
        ),
    )