import reflex as rx
import LinkBio.styles.styles as styles

def link_icon(url: str,
                text: str,
                alt: str,
                image: str = 'icons/rocketchat.svg',
                ) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=image,
            width=styles.Size.LARGE.value,
            alt=alt,
        ),
        href=url,
        text=text,
        is_external=True
    )