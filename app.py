from blog_sample.views import flaskapp, db
from blog_sample.models import Category


if __name__ == '__main__':
    #flaskapp.run(debug=True)


    # db.session.add(Category(name='esporte'))
    # db.session.add(Category(name='musica'))
    # db.session.commit()
    print(Category.query.all())
