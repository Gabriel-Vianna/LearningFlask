from flask import render_template
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from .forms import AuthorForm

flaskapp = Flask(__name__)
flaskapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
db = SQLAlchemy(flaskapp)
flaskapp.config['WTS_CSRF_ENABLED'] = True
flaskapp.config['SECRET_KEY'] = 'ao-infinito-e-alem'
from .models import Article, Author, Category


@flaskapp.route("/")
def index():
    artigos = Article.query.all()

    return render_template('index.html', titulo = 'Artigos', artigos = artigos)

@flaskapp.route("/blog/<slug>")
def article_details(slug):
    artigos = Article.query.all()
    for i in range(len(artigos)):
        if slug == artigos[i].slug:
            artigo_detalhe = artigos[i]
            return render_template('article_details.html', artigo = artigo_detalhe)
    return redirect('/404')

@flaskapp.route("/blog/<category>")
def category_details(category):
    artigos = Article.query.all()
    for i in range(len(artigos)):
        if category == artigos[i].category:
            category_detalhe = artigos[i]
            return render_template('category_details.html', artigo = category_detalhe)
    return redirect('/404')

@flaskapp.route("/blog/<author>")
def author_details(author):
    artigos = Article.query.all()
    for i in range(len(artigos)):
        if author == artigos[i].author:
            author_detalhe = artigos[i]
            return render_template('author_details.html', artigo = author_detalhe)
    return redirect('/404')

@flaskapp.route("/404")
def error_404():
    return render_template("404.html")

@flaskapp.route("/form", methods=['GET','POST'])
def form():
    author_form = AuthorForm()
    if author_form.validate_on_submit():
        print('oi')
        name = author_form.name.data
        email = author_form.email.data
        website = author_form.website.data
        photo = author_form.photo.data
        bio = author_form.bio.data
        return redirect(url_for('form'))

        # db.session.add(Author(name=name,email=email,website=website=,photo=photo,bio=bio))


    return render_template("formulário.html", form = author_form)
