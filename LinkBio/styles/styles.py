from enum import Enum
import reflex as rx
from .colors import Color, TextColor
from .fonts import Font

# Constants
MAX_WIDTH = '600px'

# Sizes
class Size(Enum):
    ZERO = '0px !important'
    SMALL = '0.5em' # em toma como referencia el tamaño de fuente
    MEDIUM = '0.8em'
    DEFAULT = '1em' # de la app
    LARGE = '1.5em'
    BIG = '2em'

# Styles : Estilos para todos los componentes
BASE_STYLES = {
    #"font_family": Font.DEFAULT.value,
    'background_color': Color.BACKGROUND.value ,
    rx.chakra.heading: {
        'color': TextColor.HEADER.value,
        #'font_family': Font.TITLE.value,
    },
    rx.chakra.Button: {
        'width': '100%',
        'height': '100%',
        'display': 'block',
        'padding': Size.SMALL.value,
        'border_radius': Size.DEFAULT.value,
        'background_color': Color.CONTENT.value,
        'color': TextColor.HEADER.value,
        '_hover': {
            'background_color': Color.SECONDARY.value
        }
    },
    rx.chakra.Link: {
        'text_decoration': 'none',
        '_hover': {}
    }
}

TITLE_STYLE = dict(
    width='100%',
    padding_top=Size.DEFAULT.value,
)

BUTTON_TITLE_STYLES = dict(
    #font_family=Font.DEFAULT.value,
    font_size=Size.DEFAULT.value,    
    color=TextColor.HEADER.value
)
BUTTON_BODY_STYLES = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)

NAVBAR_TITLE_STYLE = dict(
    font_size=Size.LARGE.value,
    #font_family=Font.LOGO.value,
)

