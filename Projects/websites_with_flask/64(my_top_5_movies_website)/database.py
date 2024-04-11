from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    class Movie(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        year = db.Column(db.Integer, nullable=False)
        title = db.Column(db.String(250), unique=True, nullable=False)
        description = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.String(250), nullable=True)
        ranking = db.Column(db.String(250), nullable=True)
        review = db.Column(db.String(250), nullable=True)
        img_url = db.Column(db.String(250), unique=True, nullable=False)

        def __repr__(self):
            return '<Movies %r>' % self.title
