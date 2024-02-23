import reflex as rx

from LinkBio.components.link_button import link_button
from LinkBio.components.title import title
import LinkBio.styles.styles as styles

def links() -> rx.Component:
    return rx.chakra.vstack(
        title('Apps con IA'),
        link_button('Chat-cv', 
                    'Chatea con mi CV',
                    'https://stm-cv.streamlit.app/'),
        link_button('Artículo Kopuru',
                    'Aprende a usar Streamlit',
                    '''https://kopuru.com/desarrollo-y-despliegue-de-modelo-de-reconocimiento-con-streamlit/'''
                    ),
        title('Apps para empresas'),
        link_button('Profile Hunter', 
                    'Caza futuros clientes',
                    'https://github.com/sertemo/ProfileHunter'),
        link_button('PesKa Mailing',
                    'Lanza mails masivos con formato',
                    '''https://talsa-mailing.streamlit.app/'''
                    ),
        link_button('Graphicator',
                    'Calcula inercias de secciones',
                    'https://graphicator.streamlit.app/'),
        width='100%',
        spacing=styles.Size.MEDIUM.value
    )