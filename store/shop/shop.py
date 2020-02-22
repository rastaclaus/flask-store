from flask import Blueprint, render_template, session, url_for
from store.models import db, ProductCategory

shop_bp = Blueprint('shop', __name__)



@shop_bp.route("/")
def index():
    cats = ProductCategory.query.all()
    return render_template('shop/index.html', cats=cats)
