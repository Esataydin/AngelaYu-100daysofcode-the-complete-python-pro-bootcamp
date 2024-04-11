from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, email


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), email()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login!")


class ItemForm(FlaskForm):
    product_name = StringField("Product Name", validators=[DataRequired()])
    product_img_url = StringField("Product Image URL")
    price = StringField("Price", validators=[DataRequired()])
    submit = SubmitField("Add New Item!")
