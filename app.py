from blog_sample.views import flaskapp, db
from blog_sample.models import Category, Author, Article


if __name__ == '__main__':
    flaskapp.run(debug=True)
