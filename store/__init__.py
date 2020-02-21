"""init store module"""
import os

from flask import Flask

from store.models import db, migrate
from store.shop import shop_bp
from store.admin import admin

def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__)

    database_fname = os.path.abspath(
        os.path.join(app.instance_path, 'store.sqlite'))

    # defaults for development
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///'+database_fname,
        SQLALCHEMY_TRACK_MODIFICATIONS=False)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    app.register_blueprint(shop_bp)

    return app
