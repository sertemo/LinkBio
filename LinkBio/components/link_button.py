import reflex as rx
import LinkBio.styles.styles as styles

def link_button(titulo: str, 
                body: str,
                url: str,
                image: str = 'icons/rocketchat.svg',
                *,
                is_external: bool = True,
                ) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.chakra.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.LARGE.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=titulo,
                    ),
                rx.chakra.vstack(
                    rx.chakra.text(titulo, 
                                    style=styles.BUTTON_TITLE_STYLES),
                    rx.chakra.text(body,
                                    style=styles.BUTTON_BODY_STYLES),
                    spacing=styles.Size.ZERO.value,
                    align_items='start',
                    margin=styles.Size.ZERO.value,
                    padding_y=styles.Size.SMALL.value,
                    padding_right=styles.Size.SMALL.value,
                ),
                width='100%'
            )
        ),
        href=url,
        is_external=is_external,
        width='100%',
        )