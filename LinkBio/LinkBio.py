"""Script principal donde se desarrolla la app."""

import reflex as rx
from  LinkBio.components.navbar import navbar
from LinkBio.views.header.header import header
from LinkBio.components.footer import footer
from LinkBio.views.links.links import links
import LinkBio.styles.styles as styles

class State(rx.State):
    pass



@rx.page(
        route="/", 
        title='Bienvenido a Sergio Tejedor',
        description='Hola, mi nombre es Sergio Tejedor. Soy ingeniero industrial y me apasiona el Machine Learning y la creación de aplicaciones.',
        image='img/stm_logo.png')
def index() -> rx.Component:
    return rx.chakra.box(
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
    )



@rx.page(route='/md', title='Render en Markdown')
def markdown_page() -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.container(
            rx.markdown(f"""{abrir_markdown()}""")
        )
    )


@rx.page(route='/about', title='Sobre mi')
def about() -> rx.Component:
    texto_sergio = rx.text('Sergio Tejedor 2024', 
                    color='red',
                    font_size='2em')
    avatar_sergio = rx.avatar(name="Sergio Tejedor")
    return rx.hstack(avatar_sergio, texto_sergio)


def abrir_markdown() -> str:
    with open('LinkBio/prueba.md', 'r') as f:
        texto = f.read()
    return texto


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES
)
# app.add_page(index, route='/') Si ponemos el decorador ya no hace falta esto
# app.add_page(about, route='/about')
# app.compile() Ya no es necesario