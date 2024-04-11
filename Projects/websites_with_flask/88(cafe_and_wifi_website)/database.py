from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db = SQLAlchemy(app)


##Cafe TABLE Configuration
with app.app_context():
    class Cafe(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(250), unique=True, nullable=False)
        map_url = db.Column(db.String(500), nullable=False)
        img_url = db.Column(db.String(500), nullable=False)
        location = db.Column(db.String(250), nullable=False)
        seats = db.Column(db.String(250), nullable=False)
        has_toilet = db.Column(db.Boolean, nullable=False)
        has_wifi = db.Column(db.Boolean, nullable=False)
        has_sockets = db.Column(db.Boolean, nullable=False)
        can_take_calls = db.Column(db.Boolean, nullable=False)
        coffee_price = db.Column(db.String(250), nullable=True)

        def to_dict(self) -> dict[str, any]:
            # Method 1.
            dictionary = {}
            # Loop through each column in the data record
            for column in self.__table__.columns:
                # Create a new dictionary entry;
                # where the key is the name of the column
                # and the value is the value of the column
                dictionary[column.name] = getattr(self, column.name)
            return dictionary

            # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
            return {column.name: getattr(self, column.name) for column in self.__table__.columns}
