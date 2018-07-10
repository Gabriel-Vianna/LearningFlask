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

admin = Admin(flaskapp, name="MyShareAdmin", template_mode="bootstrap3")

admin.add_view(ModelView(Article, db.session))
admin.add_view(AuthorView(Author, db.session))
admin.add_view(ModelView(Category, db.session))
