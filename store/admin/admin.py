from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField

from store.models import ProductCategory, db


def namegen(obj, file_data):
    return file_data.filename

class ProductCategoryModelView(ModelView):
    form_extra_fields = {
        'img': ImageUploadField(
            'Image file',
            base_path='static/images/cat',
            namegen=namegen)
    }

admin = Admin()
admin.add_view(ProductCategoryModelView(ProductCategory, db.session))
