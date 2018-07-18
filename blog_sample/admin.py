from .views import flaskapp, db
from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView
from .models import Article, Author, Category
from werkzeug.utils import secure_filename


class AuthorView(ModelView):
    form_extra_fields={'photo':form.ImageUploadField('Profile Picture',
        base_path=flaskapp.config['UPLOAD_FOLDER'])}

    def on_model_change(self, form, model, is_created=True):
        filename = secure_filename(form.photo.data.filename)
        model.photo = filename

class ArticleView(ModelView):
    form_extra_fields={'cover':form.ImageUploadField('Article Picture',
                            base_path=flaskapp.config['UPLOAD_FOLDER']),
                        'img_detail_1':form.ImageUploadField('Image Detail 1',
                            base_path=flaskapp.config['UPLOAD_FOLDER']),
                        'img_detail_2':form.ImageUploadField('Image Detail 2',
                            base_path=flaskapp.config['UPLOAD_FOLDER']),
                        'img_detail_3':form.ImageUploadField('Image Detail 3',
                            base_path=flaskapp.config['UPLOAD_FOLDER'])}

    def on_model_change(self, form, model, is_created=True):
        filename = secure_filename(form.cover.data.filename)
        model.cover = filename

admin = Admin(flaskapp, name="MyShareAdmin", template_mode="bootstrap3")

admin.add_view(ArticleView(Article, db.session))
admin.add_view(AuthorView(Author, db.session))
admin.add_view(ModelView(Category, db.session))
