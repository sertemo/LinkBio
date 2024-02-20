from enum import Enum


# Constants
MAX_WIDTH = '600px'

# Sizes
class Spacer(Enum):
    SMALL = '0.5em' # em toma como referencia el tamaño de fuente
    DEFAULT = '1em' # de la app
    BIG = '2em'