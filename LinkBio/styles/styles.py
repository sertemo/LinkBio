from enum import Enum
import reflex as rx
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = '600px'

# Fonts
STYLESHEETS = [
    'https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap'
    'https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap'
]

# Sizes
class Size(Enum):
    ZERO = '0px !important'
    SMALL = '0.5em' # em toma como referencia el tamaño de fuente
    MEDIUM = '0.8em'
    DEFAULT = '1em' # de la app
    LARGE = '1.5em'
    BIG = '2em'

class Pad(Enum):
    SMALL = '4px'
    DEFAULT = '8px'
    LARGE = '16px'

# Styles : Estilos para todos los componentes
BASE_STYLES = {
    "font_family": Font.DEFAULT.value,
    'font_weight': FontWeight.LIGHT.value,
    'background_color': Color.BACKGROUND.value ,
    rx.chakra.heading: {
        'color': TextColor.HEADER.value,
        'font_family': Font.TITLE.value,
        'font_weight': FontWeight.MEDIUM.value,
    },
    rx.chakra.Button: {
        'width': '100%',
        'height': '100%',
        'white_space': 'normal', # para que pase a dos lineas; responsive
        'padding': Size.SMALL.value,
        'border_radius': Size.DEFAULT.value,
        'background_color': Color.CONTENT.value,
        'color': TextColor.HEADER.value,
        'text_align': 'start',
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
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,    
    color=TextColor.HEADER.value
)
BUTTON_BODY_STYLES = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)

NAVBAR_TITLE_STYLE = dict(
    font_size=Size.LARGE.value,
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
)

