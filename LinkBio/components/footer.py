import reflex as rx
from datetime import datetime
import LinkBio.styles.styles as styles
from LinkBio.styles.styles import Color, TextColor
from LinkBio.components.link_icon import link_icon
import LinkBio.settings as settings


def footer() -> rx.Component:
    return rx.chakra.box(
        rx.chakra.vstack(
            link_icon(
                url=settings.REFLEX_URL, 
                text='Reflex',
                image='/icon_reflex.ico',
                alt='enlace a la página de Reflex'
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
                    href=settings.GITHUB_REPO,
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
        margin_top=styles.Size.BIG.value,
        margin_bottom='0px'
    )