from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField, SubmitField, validators
from wtforms.validators import InputRequired,Length

# User sign-up form
class createForm(FlaskForm): 
    propTitle = StringField('Property Title', validators=[
           InputRequired(),
            Length(min=3,max=30)
        ])
    desc = TextAreaField('Description', validators=[InputRequired()])

    rooms = StringField('Mo. of Rooms', validators=[
            InputRequired(),
            Length(min=3,max=30)
        ])

    btroom = StringField('Mo. of Rooms', validators=[
            InputRequired(),
            Length(min=3,max=30)
        ])

    price = StringField('Mo. of Bathrooms', validators=[
            InputRequired(),
            Length(min=3,max=30)
        ])

    pType = SelectField("Property Type", choices=[ 
        ("House"),("Apartment")])
    
    location = StringField('Location', validators=[
            InputRequired(),
            Length(min=3,max=256)
        ])
   
    photo = FileField("Photo",validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Add Property")