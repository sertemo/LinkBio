import reflex as rx
import LinkBio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            'sertemo',
        ),
        position='sticky',
        bg="lightgray",
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        z_index='999',
        align='center',
        top='0', # para que la barra siempre esté en el top de la pantalla
    )