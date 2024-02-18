import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name='Sergio Tejedor',
                    size='6'),
        rx.text('@sertemo')
    )