from enum import Enum
import reflex as rx


# Constants
MAX_WIDTH = '600px'

# Sizes
class Size(Enum):
    SMALL = '0.5em' # em toma como referencia el tamaño de fuente
    MEDIUM = '0.8em',
    DEFAULT = '1em' # de la app
    BIG = '2em'

# Styles : Estilos para todos los componentes
BASE_STYLES = {
    rx.chakra.Button: {
        'width': '100%',
        'height': '100%',
        'display': 'block',
        'padding': Size.SMALL.value,
        'border_radius': Size.DEFAULT.value
    },
    rx.chakra.Link: {
        'text_decoration': 'none',
        '_hover': {}
    }
}

TITLE_STYLE = dict(
    size='md',
    width='100%',
    padding_top=Size.DEFAULT.value
)

BUTTON_TITLE_STYLES = dict(
    font_size=Size.DEFAULT.value,    
)
BUTTON_BODY_STYLES = dict(
    font_size=Size.MEDIUM.value,
    color='#808080'
)

