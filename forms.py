from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,IntegerField,SelectField,TextAreaField
from wtforms.validators import InputRequired,Optional,Length,NumberRange,URL

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField('Species', choices =[('cat','Cat'),('dog','Dog'),('hamster','Hamster'),('fish','Fish')])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Age",validators=[Optional(),NumberRange(min=0, max=50)])

    notes = TextAreaField("Notes", validators=[Optional(), Length(min=5)])

class EditPetForm(FlaskForm):
    """Form for editing existing pets"""

    photo_url = StringField("Photo URL",validators=[Optional(), URL()])

    notes = TextAreaField("Notes", validators=[Optional(),Length(min=5)])

    available = BooleanField("Is this pet available?")