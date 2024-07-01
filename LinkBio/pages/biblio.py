"""Página donde pondré los libros que he leido y
enlaces a sus páginas de Amazon para la compra u
otro enlace referido"""

import reflex as rx

from PIL import Image

import LinkBio.settings as settings
import LinkBio.styles.styles as styles
from LinkBio.styles.colors import TextColor
from LinkBio.components.footer import footer
from LinkBio.components.navbar import navbar
from LinkBio.components.title import title
from LinkBio.components.link_button import link_button
from LinkBio.views.header import header
from LinkBio.views.links import links

@rx.page(**settings.biblio_page_config_dict)
def biblio() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                title('Bibliografía'),
                rx.chakra.text(
                    'Aquí encontrarás los libros que han servido para formarme.',
                    color=TextColor.BODY.value,
                    size=styles.Size.BIG.value,
                ),
                link_button(
                    "Aprende Python en un fin de semana",
                    "Alfredo Moreno Muñoz & Sheila Córcoles Córcoles",
                    settings.APRENDE_PYTHON,
                    Image.open("assets/icons/aprende_python.ico"),
                ),
                link_button(
                    "Python avanzado en un fin de semana",
                    "Alfredo Moreno Muñoz & Sheila Córcoles Córcoles",
                    settings.PYTHON_AVANZADO,
                    Image.open("assets/icons/aprende_python.ico"),
                ),
                link_button(
                    "Aprende SQL en un fin de semana",
                    "Antonio Padial Solier",
                    settings.SQL,
                    Image.open("assets/img/sql_fin_de_semana.jpg"),
                ),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=styles.Size.BIG.value,
                padding_left=styles.Pad.LARGE.value,
                padding_right=styles.Pad.LARGE.value,
            ),
        ),        
        footer(),
        height='100vh',
        margin_bottom=styles.Size.ZERO.value
    )