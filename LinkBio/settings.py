from LinkBio.routes import Route


INDEX_DESCRIPTION = (
    'Hola, mi nombre es Sergio Tejedor. '
    'Soy ingeniero industrial y me apasiona el Machine Learning '
    ' y la creación de aplicaciones.'

)
INDEX_TITLE = 'Sergio Tejedor | Building Your Ideas'
IMG_DESCRIPTION = 'img/stm_logo.png'

CV_PAGE_DESCRIPTION = 'Mi CV'
CV_PAGE_TITLE = 'Sergio Tejedor | Mi CV'
BIBLIO_PAGE_TITLE = 'Bibliografía'
BIBLIO_PAGE_DESCRIPTION = 'Libros leídos a día de hoy'

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

# Configuración de la página bibliografía
biblio_page_config_dict = dict(
    route=Route.BIBLIO.value,
    title=BIBLIO_PAGE_TITLE,
    description=BIBLIO_PAGE_DESCRIPTION,
    image=IMG_DESCRIPTION
)

# Enlaces
X_LINK = 'https://twitter.com/tejedormoreno'
LINKEDIN_LINK = 'http://www.linkedin.com/in/sertemo'

# Libros
APRENDE_PYTHON = 'https://www.amazon.es/Aprende-Python-en-fin-semana/dp/1719884838'
PYTHON_AVANZADO = 'https://www.amazon.es/Python-avanzado-en-fin-semana/dp/B08XLGJQQG/ref=pd_bxgy_thbs_d_sccl_1/260-4039577-9140322?pd_rd_w=eEYcU&content-id=amzn1.sym.cfceebff-276b-4b67-ad06-735b2f4350ee&pf_rd_p=cfceebff-276b-4b67-ad06-735b2f4350ee&pf_rd_r=TVPZ787ARCFBE5SEZ9S8&pd_rd_wg=sJQKM&pd_rd_r=d9c4c8b4-ff35-4fc7-83a6-0862bddf0ec2&pd_rd_i=B08XLGJQQG&psc=1'
SQL = 'https://amzn.eu/d/0iE9skxx'


REFLEX_URL = 'http://reflex.dev'
GITHUB_REPO = 'https://github.com/sertemo'
CHAT_CV_APP = 'https://stm-cv.streamlit.app/'
KOPURU_ARTICLE = 'https://kopuru.com/desarrollo-y-despliegue-de-modelo-de-reconocimiento-de-digitos-con-streamlit/'
QUIJOTE_APP = 'https://litteragpt.streamlit.app/'
CHAT_PDF_APP = 'https://q2-pdf.streamlit.app/'
SYTICO_APP = 'https://sytico.streamlit.app/'
PROFILE_HUNTER_REPO = 'https://github.com/sertemo/ProfileHunter'
TALSA_MAILING = 'https://talsa-mailing.streamlit.app/'
GRAPHICATOR_APP = 'https://graphicator.streamlit.app/'
COLLATZ_APP = 'https://collatzeral.streamlit.app/Gr%C3%A1ficos'
BBQ_BALANCE_REPO = 'https://github.com/sertemo/bbqbalance'
MECANODEI_REPO = 'https://github.com/sertemo/MecanOdei'
EARTHQUAKE = 'https://earthquakelocator.streamlit.app/'
