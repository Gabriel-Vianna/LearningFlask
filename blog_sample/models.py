from .views import db
from datetime import datetime
from .utils import html_content

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    text = db.Column(db.Text)
    abstract = db.Column(db.String(300))
    cover = db.Column(db.String(300), nullable=False)
    img_detail_1 = db.Column(db.String(300), nullable=False)
    img_detail_2 = db.Column(db.String(300), nullable=False)
    img_detail_3 = db.Column(db.String(300), nullable=False)
    published_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    published = db.Column(db.Boolean, nullable=False)
    slug = db.Column(db.String(300), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('articles', lazy=True))

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'),
        nullable=False)
    author =db.relationship('Author', backref=db.backref('authors',lazy=True))


    def __init__(self,title=None,text=None,abstract=None,cover=None, author=None, category=None, published=None, slug=None):
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

    def __repr__(datetime):
        return str(datetime.day)+"/"+str(datetime.month)+"/"+str(datetime.year)

    @property
    def formatted_text(self):
        return html_content(self.text)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    website = db.Column(db.String(30), unique=True, nullable=False)
    photo = db.Column(db.String(120), unique=False, nullable=False)
    bio = db.Column(db.String(300), unique=False, nullable=False)
    facebook = db.Column(db.String(300), unique=False)
    twitter = db.Column(db.String(300), unique=False)
    linkedin = db.Column(db.String(300), unique=False)
    github = db.Column(db.String(300), unique=False)

    def __init__(self, name='', email='', website='', photo='', bio='', facebook = '', twitter = '', linkedin = '', github = ''):
         self.name = name
         self.email = email
         self.website = website
         self.photo = photo
         self.bio = bio
         self.facebook = facebook
         self.twitter = twitter
         self.linkedin = linkedin
         self.github = github

    def __repr__(self):
        return self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return self.name

if __name__ == '__main__':
    pass
