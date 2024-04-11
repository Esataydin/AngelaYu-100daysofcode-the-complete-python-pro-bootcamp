from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


def coerce_bool(x) -> bool or None:
    if isinstance(x, str):
        return x == "True" if x != "None" else None
    else:
        return bool(x) if x is not None else None


class CafeForm(FlaskForm):

    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe Image (URL)", validators=[DataRequired(), URL()])
    location = StringField("Location(City)", validators=[DataRequired()])
    seats = StringField("How Many Seats?", validators=[DataRequired()])
    has_toilet = SelectField("Has Toilet?", choices=[(None, ""), (True, "Yes"), (False, "No")], coerce=coerce_bool)
    has_wifi = SelectField("Has Wifi?", choices=[(None, ""), (True, "Yes"), (False, "No")], coerce=coerce_bool)
    has_sockets = SelectField("Power Socket Availability", choices=[(None, ""), (True, "Yes"), (False, "No")], coerce=coerce_bool)
    can_take_calls = SelectField("Can Take Calls?", choices=[(None, ""), (True, "Yes"), (False, "No")], coerce=coerce_bool)
    coffee_price = StringField("Coffee Price?", validators=[DataRequired()])
    submit = SubmitField('Submit')