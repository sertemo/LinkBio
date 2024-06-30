import reflex as rx

from LinkBio.components.link_button import link_button
from LinkBio.components.title import title
import LinkBio.styles.styles as styles
import LinkBio.settings as settings
from LinkBio.routes import Route

def links() -> rx.Component:
    return rx.chakra.vstack(
        title('Apps con IA'),
        link_button('Chat-cv', 
                    'Chatea con mi CV',
                    settings.CHAT_CV_APP),
        link_button('Artículo Kopuru',
                    'Aprende a usar Streamlit reconociendo dígitos con IA',
                    settings.KOPURU_ARTICLE,
                    'icons/newspaper-solid.svg'
                    ),
        link_button('Littera GPT',
                    'Decoder entrenado con literatura clásica española',
                    settings.QUIJOTE_APP,
                    'icons/i-cursor-solid.svg'
                    ),
        link_button('Q2 pdf',
                    'Chatea con tus archivos pdf',
                    settings.CHAT_PDF_APP,
                    'icons/file-circle-question-solid.svg'),
        link_button('SyTiCo',
                    'Resume el contenido de un video de YouTube',
                    settings.SYTICO_APP,
                    'icons/youtube.svg'),
        title('Apps para empresas'),
        link_button('Profile Hunter', 
                    'Caza futuros clientes',
                    settings.PROFILE_HUNTER_REPO,
                    'icons/bullseye-solid.svg'),
        link_button('PsK Mailing',
                    'Lanza mails masivos con formato',
                    settings.TALSA_MAILING,
                    'icons/fish-fins-solid.svg'
                    ),
        link_button('Graphicator',
                    'Calcula inercias de secciones',
                    settings.GRAPHICATOR_APP,
                    'icons/compass-drafting-solid.svg'),
        title('Apps Variadas'),
        link_button('Collatz',
                    'Juega con la conjetura de Collatz',
                    settings.COLLATZ_APP,
                    'icons/1-solid.svg'),
        link_button('BBQ Balance',
                    'Ajusta cuentas con tu cuadrilla',
                    settings.BBQ_BALANCE_REPO,
                    'icons/scale-balanced-solid.svg'),
        link_button('MecanOdei',
                    'Mejora tu mecanografía',
                    settings.MECANODEI_REPO,
                    'icons/keyboard-solid.svg'),
        link_button('EarthQuake Locator',
                    'Localiza terremotos en todo el globo',
                    settings.EARTHQUAKE,
                    'icons/earth-americas-solid.svg'),
        title('Mi CV'),
        link_button('Currículo',
                    'Accede a mi CV detallado',
                    Route.CV.value,
                    'icons/file-solid.svg',
                    is_external=False),
        title('Bibliografía'),
        link_button(
            "Bibliografía",
            "Explora los libros que he leído hasta la fecha",
            Route.BIBLIO.value,
            'icons/book-solid.svg',
            is_external=False
        ),
        width='100%',
        spacing=styles.Size.MEDIUM.value
    )