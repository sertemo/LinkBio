import reflex as rx
from LinkBio.components.link_icon import link_icon
from LinkBio.components.info_text import info_text
import LinkBio.styles.styles as styles
from LinkBio.styles.styles import Color, TextColor
import LinkBio.settings as settings

def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(
                src='img/logo STM inverted colors.jpg',
                name='Sergio Tejedor',
                size='xl',
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding='4px',
                border='4px',
                border_color=Color.SECONDARY.value,
                ),          
            rx.chakra.vstack(
                rx.chakra.heading(
                    'Sergio Tejedor',
                    ),
                rx.chakra.link(
                    rx.chakra.text(
                        '@TejedorMoreno',
                        margin_top=styles.Size.ZERO.value,
                        color=Color.SECONDARY.value),
                        is_external=True,
                        href=settings.X_LINK
                ),
                rx.chakra.hstack(
                    link_icon(
                        url=settings.GITHUB_REPO, 
                        text='GitHub',
                        image='/icons/github.svg',
                        alt='enlace a Github'
                        ),
                    link_icon(
                        url=settings.LINKEDIN_LINK, 
                        text='Linkdin',
                        image='/icons/linkedin.svg',
                        alt='enlace a mi Linkedin'
                        ),
                    spacing=styles.Size.MEDIUM.value,
                ),
                align_items='start',
            ),
            spacing=styles.Size.BIG.value
        ),
        rx.chakra.flex(
            info_text('+2', 'años de experiencia'),
            rx.chakra.spacer(),
            info_text('+10', 'aplicaciones'),
            rx.chakra.spacer(),
            info_text('+100', 'ganas de aprender'),
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
                ido desarrollando.""",
                color=TextColor.BODY.value,
                font_size=styles.Size.MEDIUM.value
                ),
        align_items='start',
        spacing=styles.Size.BIG.value,        
    )