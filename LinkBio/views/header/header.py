import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.chakra.avatar(name='Sergio Tejedor',
                    size='xl',
                    ),
        rx.text('@TejedorMoreno'),
        rx.text('HOLA 👋 MI NOMBRE ES SERGIO TEJEDOR'),
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
        align='center',
    )