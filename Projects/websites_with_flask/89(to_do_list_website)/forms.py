from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


def coerce_bool(x) -> bool or None:
    if isinstance(x, str):
        return x == "True" if x != "None" else None
    else:
        return bool(x) if x is not None else None


class TodoForm(FlaskForm):

    topic = StringField('Topic', validators=[DataRequired()])
    content = StringField("Content")
    is_going = SelectField("Is Going?", choices=[(False, ""), (True, "Yes"), (False, "No")], coerce=coerce_bool)
    is_done = SelectField("Is Done?", choices=[(False, ""), (True, "Yes"), (False, "No")], coerce=coerce_bool)
    submit = SubmitField('Submit')
