from blog_sample.views import flaskapp, db
# from blog_sample.admin import admin
from blog_sample.models import Article,Author,Category
from flask_frozen import Freezer

freezer = Freezer(flaskapp)

if __name__ == '__main__':
    # flaskapp.run(debug=True)
    freezer.run()
    # db.session.add(Article(title='RPG de mesa baseado em The Witcher ganha data de lançamento', text='A R. Talsorian Games anunciou que seu RPG de mesa baseado na franquia The Witcher finalmente tem data para ser lançado. O jogo chega oficialmente no evento Gen Con 2018, que acontece em Indianápolis, nos EUA, entre 2 e 5 de agosto. O RPG foi anunciado originalmente em 2015 e segue os eventos dos jogos eletrônicos, se passando entre The Witcher 2 e The Witcher 3.',abstract="A R. Talsorian Games anunciou que seu RPG de mesa baseado na franquia The Witcher finalmente tem data para ser lançado...", cover='cover.png', published=True, slug='rpg-de-mesa-baseado-em-The-Witcher-ganha-data-de-lançamento', category=Category(name='Jogos'), author=Author(name='Gabriel Andrade Vianna',email='gabriel.vianna@original.io', website='gabrielvianna.com.br', photo='gabriel.png', bio= 'Leitor de HQ')))
    # db.session.commit()
    # print(Category.query.all())
