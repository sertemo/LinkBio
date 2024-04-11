"""Devuelve el componente script para indicar el idioma de la página"""

import reflex as rx

def lang() -> rx.Component:
    """Devuelve el idioma de la página"""
    return rx.script("document.documentElement.lang='es'")