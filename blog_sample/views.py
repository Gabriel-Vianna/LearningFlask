from flask import render_template
from flask import Flask
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

flaskapp = Flask(__name__)
flaskapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
db = SQLAlchemy(flaskapp)

from .models import Article, Author, Category




# artigos = [Article("Copa do mundo", "Esse ano a copa do mundo será na Russia....", "A copa do mundo na Russia...", "cover.png", "01/06/2018", "Gabriel Vianna", "07/06/2018", "Futebol", "sim", "copa-do-mundo"),
#           Article("Framework Flask", "Esse ano a copa do mundo será na Russia....", "A copa do mundo na Russia...", "cover.png", "01/06/2018", "Hallison Paz", "07/06/2018", "Tecnologia", "sim", "framework-flask"),
#           Article("Aulas de física", "Esse ano a copa do mundo será na Russia....", "A copa do mundo na Russia...", "cover.png", "01/06/2018", "Allan Vitor", "07/06/2018", "Ciências", "sim", "aulas-de-fisica")
#           ]

@flaskapp.route("/")
def index():
    return render_template('index.html', titulo = 'Artigos', artigos = artigos)

@flaskapp.route("/blog/<slug>")
def details(slug):
    for i in range(len(artigos)):
        if slug == artigos[i].slug:
            artigo_detalhe = artigos[i]
            return render_template('details.html', artigo = artigo_detalhe)
    return redirect('/404')

@flaskapp.route("/404")
def error_404():
    return render_template("404.html")
