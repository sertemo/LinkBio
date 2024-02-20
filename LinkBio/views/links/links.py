import reflex as rx

from LinkBio.components.link_button import link_button

def links() -> rx.Component:
    return rx.chakra.vstack(
        link_button('Chat-cv', 'https://stm-cv.streamlit.app/'),
        link_button('Artículo Kopuru', 
                    '''https://kopuru.com/desarrollo-y-despliegue-de-modelo-de-reconocimiento-con-streamlit/'''),
    )