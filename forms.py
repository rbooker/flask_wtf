from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Add a pet"""
    name = StringField("Pet Name",  validators=[InputRequired(message="Pet Name can't be blank")])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Please provide a valid URL")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Edit a pet"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Please provide a valid URL")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available?")