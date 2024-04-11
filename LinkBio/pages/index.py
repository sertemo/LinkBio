"""Página index de la web con todos los enlaces a mis apps"""

import reflex as rx
from  LinkBio.components.navbar import navbar
from LinkBio.components.idioma import lang
from LinkBio.components.footer import footer
from LinkBio.views.header import header
from LinkBio.views.links import links
import LinkBio.settings as settings
import LinkBio.styles.styles as styles

@rx.page(**settings.index_page_config_dict)
def index() -> rx.Component:
    return rx.chakra.box(
        lang(),
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=styles.Size.BIG.value,
                padding_left=styles.Pad.LARGE.value,
                padding_right=styles.Pad.LARGE.value,
            ),
        ),        
        footer(),
        height='100%',
        margin_bottom=styles.Size.ZERO.value
    )