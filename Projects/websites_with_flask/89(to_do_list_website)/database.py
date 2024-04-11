from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db = SQLAlchemy(app)

with app.app_context():
    class List(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        topic = db.Column(db.String(50), nullable=False)
        date = db.Column(db.String(50), nullable=False)
        content = db.Column(db.String(250))
        is_going = db.Column(db.Boolean, nullable=False)
        is_done = db.Column(db.Boolean, nullable=False)

    db.create_all()
