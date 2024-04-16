import reflex as rx
import LinkBio.styles.styles as styles
from LinkBio.styles.styles import TextColor, Color
from LinkBio.routes import Route
from LinkBio.components.ant_components import float_button

def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.link(
        rx.chakra.box(
            rx.chakra.span('ser', color=Color.PRIMARY.value),
            rx.chakra.span('temo', color=Color.SECONDARY.value),
            style=styles.NAVBAR_TITLE_STYLE,            
            ),
            href=Route.INDEX.value
        ),
        float_button(
            icon=rx.chakra.Image(src='/icons/question-solid.svg'),
            href=Route.CV.value,
            tooltip='Preguntas y respuestas'
        ),
        position='sticky',
        bg=Color.CONTENT.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.SMALL.value,
        z_index='999',
        align='center',
        top='0', # para que la barra siempre esté en el top de la pantalla
    )