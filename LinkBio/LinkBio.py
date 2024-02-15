"""Script principal donde se desarrolla la app."""

import reflex as rx

class State(rx.State):
    pass

class BotonAbout(rx.State):
    color_scheme = 'red'

    def flip_color(self) -> None:
        if self.color_scheme == 'red':
            self.color_scheme = 'blue'
        else:
            self.color_scheme = 'red'

def abrir_markdown() -> str:
    with open('LinkBio/prueba.md', 'r') as f:
        texto = f.read()
    return texto

@rx.page(route="/", title="Página Principal")
def index() -> rx.Component:
    boton_about = rx.button("About",
                            border_radius="1em",
                            color_scheme=BotonAbout.color_scheme,
                            size='sm',
                            variant='ghost',
                            on_click=BotonAbout.flip_color,
                            _hover={
                                'opacity': 1
                            })
    texto = rx.text('Página Principal')
    return rx.vstack(texto, boton_about, align_items="start")

@rx.page(route='/md', title='Render en Markdown')
def markdown_page() -> rx.Component:
    return rx.markdown(f"""{abrir_markdown()}""")

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