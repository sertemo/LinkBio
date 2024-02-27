from enum import Enum
import reflex as rx

class Color(Enum):
    PRIMARY = "#14a1f0" # Color del logotipo
    SECONDARY = "#087ec4" # Sombra del logotipo 
    BACKGROUND = "#0C151D" # Azul muy oscuro
    CONTENT = "#171F26" # azul mas grisaceo

class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#C3C7CB"
    FOOTER = "#A3ABB2"
