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
                rx.spacer(spacing='9'),
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
                link_button(
                    "Python para todos",
                    "Charles Severance",
                    settings.PYTHON_PARA_TODOS,
                    Image.open("assets/img/python_para_todos.jpg"),
                ),
                link_button(
                    "Neural Networks from Scratch in Python",
                    "Harrison Kinsley & Daniel Kukiela",
                    settings.PYTHON_PARA_TODOS,
                    Image.open("assets/img/nnfs.webp"),
                ),
                link_button(
                    "Curso intensivo de Python",
                    "Eric Matthes",
                    settings.CURSO_INT_PYTHON,
                    Image.open("assets/img/curso_int_python.jpg"),
                ),
                link_button(
                    "Python tricks the book",
                    "Dan Bader",
                    settings.PYTHON_TRICKS,
                    Image.open("assets/img/python_tricks.jpg"),
                ),
                link_button(
                    "Effective Python",
                    "Brett Slatkin",
                    settings.EFFECTIVE_PYTHON,
                    Image.open("assets/img/effective_python.jpg"),
                ),
                link_button(
                    "Building Data Science Applications with FastAPI",
                    "François Voron",
                    settings.FASTAPI_DATA_SCIENCE,
                    Image.open("assets/img/fastapi.jpg"),
                ),
                link_button(
                    "Machine Learning with PyTorch and Scikit-Learn",
                    "Sebastian Raschka",
                    settings.ML_W_PYTORCH,
                    Image.open("assets/img/ml_w_pytorch.jpg"),
                ),
                link_button(
                    "Git GitHub desde cero",
                    "Brais Moure",
                    settings.GITHUB_DSD_CERO,
                    Image.open("assets/img/github_dsd_cero.jpg"),
                ),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=styles.Size.BIG.value,
                padding_left=styles.Pad.LARGE.value,
                padding_right=styles.Pad.LARGE.value,
                spacing=styles.Size.DEFAULT.value
            ),
        ),        
        footer(),
        height='100%',
        margin_bottom=styles.Size.ZERO.value
    )