import reflex as rx
import LinkBio.styles.styles as styles

def link_icon(url: str, text: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.icon(
            tag='link'
        ),
        href=url,
        text=text,
        is_external=True
    )