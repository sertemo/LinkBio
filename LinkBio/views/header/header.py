import reflex as rx
from LinkBio.components.link_icon import link_icon
from LinkBio.components.info_text import info_text
import LinkBio.styles.styles as styles

def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(
                name='Sergio Tejedor',
                size='xl'),
            rx.chakra.vstack(
                rx.chakra.heading(
                    'Sergio Tejedor',
                    size='lg'),
                rx.chakra.text(
                    '@TejedorMoreno',
                    margin_top='0px !important'),
                rx.chakra.hstack(
                    link_icon('http://github.com/sertemo', 'GitHub'),
                    link_icon('http://github.com/sertemo', 'Linkdin')
                ),
                align_items='start'
            ),
            spacing=styles.Size.BIG.value
        ),
        rx.chakra.flex(
            info_text('+1', 'años de experiencia'),
            rx.chakra.spacer(),
            info_text('+1', 'años de experiencia'),
            rx.chakra.spacer(),
            info_text('+1', 'años de experiencia'),
            width='100%'
        ),
        rx.text("""Soy un ingeniero industrial apasionado por el Machine 
                Learning, la programación en Python y el desarrollo de 
                aplicaciones. Dirijo el departamento técnico de un grupo 
                empresarial especializado en la laminación de perfiles en frío y
                fabricación de invernaderos industriales. Actualmente, 
                estoy expandiendo mis habilidades a través de un bootcamp 
                intensivo en ciencia de datos.
                Aquí podrás encontrar una lista de aplicaciones que he
                ido desarrollando."""
                ),
        align_items='start',
        spacing=styles.Size.BIG.value
    )