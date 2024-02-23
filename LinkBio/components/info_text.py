import reflex as rx
import LinkBio.styles.styles as styles


def info_text(title: str, body: str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(title, font_weight='bold', color='blue'),
        ' ',
        body,
        font_size=styles.Size.MEDIUM.value
    )