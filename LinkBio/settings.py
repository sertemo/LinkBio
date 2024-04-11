from LinkBio.routes import Route


INDEX_DESCRIPTION = 'Hola, mi nombre es Sergio Tejedor. Soy ingeniero industrial y me apasiona el Machine Learning y la creación de aplicaciones.'
INDEX_TITLE = 'Sergio Tejedor | Building Your Ideas'
IMG_DESCRIPTION = 'img/stm_logo.png'

CV_PAGE_DESCRIPTION = 'Mi CV'
CV_PAGE_TITLE = 'Sergio Tejedor | Mi CV'

# Configuración página principal
index_page_config_dict = dict(
    route=Route.INDEX.value,
    title=INDEX_TITLE,
    description=INDEX_DESCRIPTION,
    image=IMG_DESCRIPTION
)

# Configuración de CV
cv_page_config_dict = dict(
    route=Route.CV.value,
    title=CV_PAGE_TITLE,
    description=CV_PAGE_DESCRIPTION,
    image=IMG_DESCRIPTION
)

# Enlaces
X_LINK = 'https://twitter.com/tejedormoreno'
LINKEDIN_LINK = 'http://www.linkedin.com/in/sertemo'

REFLEX_URL = 'http://reflex.dev'
GITHUB_REPO = 'https://github.com/sertemo'
CHAT_CV_APP = 'https://stm-cv.streamlit.app/'
KOPURU_ARTICLE = 'https://kopuru.com/desarrollo-y-despliegue-de-modelo-de-reconocimiento-de-digitos-con-streamlit/'
QUIJOTE_APP = ''
CHAT_PDF_APP = 'https://q2-pdf.streamlit.app/'
SYTICO_APP = 'https://sytico.streamlit.app/'
PROFILE_HUNTER_REPO = 'https://github.com/sertemo/ProfileHunter'
TALSA_MAILING = 'https://talsa-mailing.streamlit.app/'
GRAPHICATOR_APP = 'https://graphicator.streamlit.app/'
COLLATZ_APP = 'https://collatzeral.streamlit.app/Gr%C3%A1ficos'
BBQ_BALANCE_REPO = 'https://github.com/sertemo/bbqbalance'
MECANODEI_REPO = 'https://github.com/sertemo/MecanOdei'
