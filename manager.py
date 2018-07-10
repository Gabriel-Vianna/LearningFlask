from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from blog_sample.views import flaskapp, db

flaskapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

migrate = Migrate(flaskapp, db)

manager = Manager(flaskapp)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
