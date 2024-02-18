"""Script principal donde se desarrolla la app."""

import reflex as rx
from  LinkBio.components.navbar import navbar
from LinkBio.views.header.header import header

class State(rx.State):
    pass


def abrir_markdown() -> str:
    with open('LinkBio/prueba.md', 'r') as f:
        texto = f.read()
    return texto


@rx.page(route="/", title='Bienvenido a Sergio Tejedor')
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
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

app = rx.App()
# app.add_page(index, route='/') Si ponemos el decorador ya no hace falta esto
# app.add_page(about, route='/about')
# app.compile() Ya no es necesario