"""Scripts para integrar componentes de ant design

https://ant.design
"""

import reflex as rx
from LinkBio.styles.colors import Color


class FloatButton(rx.Component):
    """Crea un floatbuttom de ant design.
    Es un componente de React.
    Solo necesitamos la library y el tag
    para crearlo en Reflex.
    
    El FloatButtom aparecerá siempre abajo
    a la derecha"""

    library = "antd"
    tag = "FloatButton"
    icon: rx.Var[rx.chakra.Image]
    href: rx.Var[str]
    target = '_blank'
    badge = {
        "dot": True,
        "color": Color.PRIMARY.value
    }   
    tooltip: rx.Var[str]

float_button = FloatButton.create