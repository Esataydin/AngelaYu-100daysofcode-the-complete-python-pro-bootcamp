from flask import Flask
from flask_login import UserMixin
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    cart = relationship("Cart", back_populates="cart_owner")


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)

    product_name = db.Column(db.String(100))
    product_id = db.Column(db.String(100))
    product_img_url = db.Column(db.String(250))
    price = db.Column(db.Integer)
    price_id = db.Column(db.String(100))


class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    cart_owner = relationship("User", back_populates="cart")

    item_id = db.column(db.Integer)
    product_name = db.Column(db.String(100))
    product_id = db.Column(db.String(100))
    product_img_url = db.Column(db.String(250))
    price = db.Column(db.Integer)
    price_id = db.Column(db.String(100))


with app.app_context():
    db.create_all()
