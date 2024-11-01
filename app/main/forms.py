from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class PlayerCountForm(FlaskForm):
    number = SelectField(label="Liars", choices=[(i + 1, str(i + 1)) for i in range(6)])
    submit = SubmitField(label="Submit")


class PlayerNameForm(FlaskForm):
    submit = SubmitField(label="Submit")

    @classmethod
    def append_class(cls, players: dict):
        for k, v in players.items():
            setattr(cls, k, StringField(
                validators=[DataRequired()],
                render_kw={"placeholder": v, "autocomplete": "off"})
                    )
        return cls
