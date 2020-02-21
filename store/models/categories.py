"""Product category model module"""
from .db import db

class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True, index=True)
    image_small = db.LargeBinary()
