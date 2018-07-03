from .views import db
from datetime import datetime


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    abstract = db.Column(db.String(50), nullable=False)
    cover = db.Column(db.String(50), nullable=False)
    published_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    published = db.Column(db.Boolean, nullable=False)
    slug = db.Column(db.String(50), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('articles', lazy=True))

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'),
        nullable=False)
    author =db.relationship('Author', backref=db.backref('authors',lazy=True))


    def __init__(self,title,text,abstract,cover, author, category, published, slug):
        self.title = title
        self.text = text
        self.abstract = abstract
        self.cover = cover
        self.author = author
        self.category = category
        self.published = published
        self.slug = slug


    def __str__(self):
        res = str(self.title)+"/"+str(self.abstract)
        return res

    def __repr__(self):
        return self.title

"""class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username"""

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    website = db.Column(db.String(30), unique=True, nullable=False)
    photo = db.Column(db.String(120), unique=False, nullable=False)
    bio = db.Column(db.String(300), unique=False, nullable=False)

    def __init__(self, name, email, website, photo, bio):
         self.name = name
         self.email = email
         self.website = website
         self.photo = photo
         self.bio = bio

    def __repr__(self):
        return self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

if __name__ == '__main__':
    pass
