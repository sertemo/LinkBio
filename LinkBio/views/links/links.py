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
                    'Aprende a usar Streamlit reconociendo dígitos con IA',
                    '''https://kopuru.com/desarrollo-y-despliegue-de-modelo-de-reconocimiento-con-streamlit/'''
                    ),
        link_button('Quijote GPT',
        'Decoder entrenado con el Quijote',
        ''''''
                    ),
        link_button('Q2 pdf',
                    'Chatea con tus archivos pdf',
                    'https://q2-pdf.streamlit.app/'),
        link_button('SyTiCo',
                    'Resume el contenido de un video de YouTube',
                    'https://sytico.streamlit.app/'),
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
        title('Apps Variadas'),
        link_button('Collatz',
                    'Juega con la conjetura de Collatz',
                    'https://collatzeral.streamlit.app/Gr%C3%A1ficos'),
        link_button('BBQ Balance',
                    'Ajusta cuentas con tu cuadrilla',
                    'https://github.com/sertemo/bbqbalance'),
        link_button('MecanOdei',
                    'Mejora tu mecanografía',
                    'https://github.com/sertemo/MecanOdei'),
        width='100%',
        spacing=styles.Size.MEDIUM.value
    )