import reflex as rx
import LinkBio.styles.styles as styles

def link_button(titulo: str, 
                body: str,
                url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.icon(tag='chevrons-right',
                                size=20,
                                ),
                rx.chakra.vstack(
                    rx.chakra.text(titulo, 
                                    style=styles.BUTTON_TITLE_STYLES),
                    rx.chakra.text(body,
                                    style=styles.BUTTON_BODY_STYLES),
                    align_items='start',
                ),
            )
        ),
        href=url,
        is_external=True,
        width='100%',
        )