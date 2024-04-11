"""Página donde pondré mi CV actualizado"""

import reflex as rx

import LinkBio.settings as settings
import LinkBio.styles.styles as styles
from LinkBio.components.footer import footer
from LinkBio.components.navbar import navbar
from LinkBio.components.title import title
from LinkBio.views.header import header
from LinkBio.views.links import links

@rx.page(**settings.cv_page_config_dict)
def cv() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                title('mi CV'),
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