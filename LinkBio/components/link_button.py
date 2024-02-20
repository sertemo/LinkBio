import reflex as rx

def link_button(texto: str, url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(texto, width='100%'),
        href=url,
        is_external=True,
        width='100%',
        )