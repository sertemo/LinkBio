import reflex as rx
import LinkBio.styles.styles as styles
from LinkBio.styles.styles import TextColor, Color


def info_text(title: str, body: str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(
            title,
            font_weight='bold',
            color=Color.SECONDARY.value),
        ' ',
        body,
        font_size=styles.Size.MEDIUM.value,
        color=TextColor.BODY.value
    )