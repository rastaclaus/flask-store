import os

from jinja2 import Markup
from flask import current_app as app, url_for

from flask_admin import Admin, form, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField

from store.models import ProductCategory, db
admin = Admin(
        index_view=AdminIndexView(
            name='Администрирование',
            url='/mod'))


def _list_thumbnail(view, context, model, name):
    if not model.image:
        return ''

    return Markup('<img src="{}">'.format(
        url_for('static', filename='images/cat/'+form.thumbgen_filename(model.image))
    ))

class ProductCategoryModelView(ModelView):
    column_formatters = {'image': _list_thumbnail}

    form_extra_fields = {
        'image': form.ImageUploadField(
            'Image',
            base_path='store/static/images/cat',
            thumbnail_size=(100, 100, True),
            url_relative_path='images/cat/')
    }


admin.add_view(ProductCategoryModelView(ProductCategory, db.session))
