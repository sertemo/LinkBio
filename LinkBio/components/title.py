import reflex as rx
import LinkBio.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.chakra.heading(
        text,
        size='lg',
        width='100%',
        style=styles.TITLE_STYLE
    )