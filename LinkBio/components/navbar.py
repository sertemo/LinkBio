import reflex as rx
import LinkBio.styles.styles as styles
from LinkBio.styles.styles import TextColor, Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.chakra.box(
            rx.chakra.span('ser', color=Color.PRIMARY.value),
            rx.chakra.span('temo', color=Color.SECONDARY.value),
            style=styles.NAVBAR_TITLE_STYLE,       
            
        ),
        position='sticky',
        bg=Color.CONTENT.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.SMALL.value,
        z_index='999',
        align='center',
        top='0', # para que la barra siempre esté en el top de la pantalla
    )