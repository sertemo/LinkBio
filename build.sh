# Script para automatizar los procesor en consola
# y crear una carpeta public para subir a github
# con todo el contenido del front para vincular
# con vercel
#source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
git add .
git commit -m "automatizado"
git push
#deactivate