"""Script principal donde se desarrolla la app."""

import reflex as rx

from LinkBio.pages.cv import cv
from LinkBio.pages.index import index
from LinkBio.pages.biblio import biblio
import LinkBio.styles.styles as styles

class State(rx.State):
    pass


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES
)
# app.add_page(index, route='/') Si ponemos el decorador ya no hace falta esto
# app.add_page(about, route='/about')
# app.compile() Ya no es necesario